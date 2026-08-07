document.addEventListener('DOMContentLoaded', () => {
  if (document.body.classList.contains('page-stretches')) {
    setupStretchPage();
  }

  if (document.body.classList.contains('page-alarms')) {
    setupAlarmPage();
  }
});

function setupStretchPage() {
  const filterButtons = Array.from(document.querySelectorAll('.filter-pill'));
  const cards = Array.from(document.querySelectorAll('.stretch-card'));
  const reviewButtons = Array.from(document.querySelectorAll('button[data-save-target]'));
  const storagePrefix = 'stretchitout-review-';

  const getStorageKey = (targetId) => `${storagePrefix}${targetId}`;

  const saveReview = (targetId, rating, note) => {
    try {
      window.localStorage.setItem(getStorageKey(targetId), JSON.stringify({ rating, note }));
    } catch (error) {
      console.warn('Unable to save review', error);
    }
  };

  const restoreReview = (targetId, noteId, savedReview) => {
    try {
      const raw = window.localStorage.getItem(getStorageKey(targetId));
      if (!raw) {
        return;
      }

      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== 'object') {
        return;
      }

      const ratingInput = document.getElementById(targetId);
      const noteInput = document.getElementById(noteId);

      if (ratingInput) {
        ratingInput.value = parsed.rating ?? ratingInput.value;
      }

      if (noteInput) {
        noteInput.value = parsed.note ?? '';
      }

      if (savedReview) {
        savedReview.textContent = `Saved review: ${parsed.rating ?? 5}/5 — ${parsed.note || 'No extra note provided.'}`;
      }
    } catch (error) {
      console.warn('Unable to restore review', error);
    }
  };

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      filterButtons.forEach((item) => item.classList.remove('active'));
      button.classList.add('active');
      const selected = button.dataset.filter;

      cards.forEach((card) => {
        const matches = selected === 'all' || card.dataset.category === selected;
        card.style.display = matches ? 'block' : 'none';
      });
    });
  });

  reviewButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const targetId = button.dataset.saveTarget;
      const noteId = button.dataset.noteTarget;
      const ratingInput = document.getElementById(targetId);
      const noteInput = document.getElementById(noteId);
      const savedReview = document.getElementById(`saved-${targetId.replace('rating-', '')}`);

      if (!ratingInput || !noteInput || !savedReview) {
        return;
      }

      const rating = Number(ratingInput.value);
      const note = noteInput.value.trim() || 'No extra note provided.';
      const safeRating = Number.isFinite(rating) ? Math.min(5, Math.max(1, Math.round(rating))) : 5;
      savedReview.textContent = `Saved review: ${safeRating}/5 — ${note}`;
      saveReview(targetId, safeRating, note);
    });
  });

  reviewButtons.forEach((button) => {
    const targetId = button.dataset.saveTarget;
    const noteId = button.dataset.noteTarget;
    const savedReview = document.getElementById(`saved-${targetId.replace('rating-', '')}`);

    if (targetId && noteId && savedReview) {
      restoreReview(targetId, noteId, savedReview);
    }
  });
}

function setupAlarmPage() {
  const scheduleMode = document.getElementById('scheduleMode');
  const hoursSettings = document.getElementById('hoursSettings');
  const daysSettings = document.getElementById('daysSettings');
  const dateTimeSettings = document.getElementById('dateTimeSettings');
  const hoursInput = document.getElementById('hours');
  const daysInput = document.getElementById('days');
  const dayTimeInput = document.getElementById('dayTime');
  const reminderDateInput = document.getElementById('reminderDate');
  const reminderTimeInput = document.getElementById('reminderTime');
  const addDateTimeButton = document.getElementById('addDateTime');
  const scheduleList = document.getElementById('scheduleList');
  const titleInput = document.getElementById('title');
  const softSoundInput = document.getElementById('softSound');
  const startBtn = document.getElementById('startBtn');
  const stopBtn = document.getElementById('stopBtn');
  const statusEl = document.getElementById('status');
  const messageEl = document.getElementById('message');

  let activeTimers = [];
  let repeatingTimer = null;
  let scheduledDateTimes = [];

  function updateVisibleSettings() {
    hoursSettings.classList.toggle('hidden', scheduleMode.value !== 'hours');
    daysSettings.classList.toggle('hidden', scheduleMode.value !== 'days');
    dateTimeSettings.classList.toggle('hidden', scheduleMode.value !== 'datetime');
  }

  function setInitialDateTime() {
    const now = new Date();
    reminderDateInput.value = now.toISOString().slice(0, 10);
    reminderTimeInput.value = now.toTimeString().slice(0, 5);
  }

  function formatScheduleItem(date) {
    return date.toLocaleString([], { dateStyle: 'medium', timeStyle: 'short' });
  }

  function renderScheduleList() {
    scheduleList.innerHTML = '';
    scheduledDateTimes.sort((a, b) => a.getTime() - b.getTime()).forEach((date, index) => {
      const item = document.createElement('li');
      item.className = 'schedule-item';
      const label = document.createElement('span');
      label.textContent = formatScheduleItem(date);
      const remove = document.createElement('button');
      remove.type = 'button';
      remove.textContent = 'Remove';
      remove.addEventListener('click', () => {
        scheduledDateTimes.splice(index, 1);
        renderScheduleList();
      });
      item.append(label, remove);
      scheduleList.appendChild(item);
    });
  }

  function addDateTimeReminder() {
    const dateValue = reminderDateInput.value;
    const timeValue = reminderTimeInput.value;
    if (!dateValue || !timeValue) {
      messageEl.textContent = 'Please choose both a date and a time.';
      return;
    }

    const date = new Date(`${dateValue}T${timeValue}:00`);
    if (Number.isNaN(date.getTime())) {
      messageEl.textContent = 'That date/time is invalid.';
      return;
    }
    if (date.getTime() <= Date.now()) {
      messageEl.textContent = 'Please choose a future date and time.';
      return;
    }

    scheduledDateTimes.push(date);
    renderScheduleList();
    messageEl.textContent = 'Date/time reminder added.';
  }

  function requestNotificationPermission() {
    if ('Notification' in window && Notification.permission === 'default') {
      Notification.requestPermission().catch(() => {});
    }
  }

  function playSoftSound() {
    if (!softSoundInput.checked) {
      return;
    }
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) {
      return;
    }
    const context = new AudioContext();
    const oscillator = context.createOscillator();
    const gain = context.createGain();
    oscillator.type = 'sine';
    oscillator.frequency.value = 660;
    gain.gain.value = 0.03;
    oscillator.connect(gain);
    gain.connect(context.destination);
    oscillator.start();
    gain.gain.exponentialRampToValueAtTime(0.00001, context.currentTime + 0.5);
    oscillator.stop(context.currentTime + 0.5);
    context.close().catch(() => {});
  }

  function showNotification() {
    const title = titleInput.value.trim() || 'Time to stretch';
    const body = 'Stand up, roll your shoulders, and take a few slow breaths.';
    if ('Notification' in window && Notification.permission === 'granted') {
      new Notification(title, { body, tag: 'stretch-reminder' });
    } else {
      window.alert(`${title}\n${body}`);
    }
    playSoftSound();
    statusEl.textContent = 'Status: reminder triggered';
    messageEl.textContent = `${title}: ${body}`;
  }

  function clearTimers() {
    if (repeatingTimer) {
      clearTimeout(repeatingTimer);
      clearInterval(repeatingTimer);
      repeatingTimer = null;
    }
    activeTimers.forEach((timerId) => clearTimeout(timerId));
    activeTimers = [];
  }

  function scheduleHourlyReminder() {
    const hours = Math.max(1, Number(hoursInput.value) || 1);
    const delay = hours * 60 * 60 * 1000;
    repeatingTimer = window.setTimeout(function tick() {
      showNotification();
      repeatingTimer = window.setTimeout(tick, delay);
    }, delay);
    statusEl.textContent = 'Status: running';
    messageEl.textContent = `Reminder every ${hours} hour${hours === 1 ? '' : 's'}.`;
  }

  function scheduleDailyReminder() {
    const days = Math.max(1, Number(daysInput.value) || 1);
    const [hour, minute] = dayTimeInput.value.split(':').map(Number);
    const now = new Date();
    const next = new Date(now);
    next.setHours(hour, minute, 0, 0);
    if (next.getTime() <= now.getTime()) {
      next.setDate(next.getDate() + days);
    }
    const delay = next.getTime() - now.getTime();

    const scheduleNext = () => {
      showNotification();
      repeatingTimer = window.setTimeout(scheduleNext, days * 24 * 60 * 60 * 1000);
    };

    repeatingTimer = window.setTimeout(scheduleNext, delay);
    statusEl.textContent = 'Status: running';
    messageEl.textContent = `Reminder every ${days} day${days === 1 ? '' : 's'} at ${dayTimeInput.value}.`;
  }

  function scheduleDateTimeReminders() {
    if (!scheduledDateTimes.length) {
      messageEl.textContent = 'Add at least one date and time before starting.';
      return;
    }

    scheduledDateTimes.forEach((date) => {
      const delay = date.getTime() - Date.now();
      if (delay > 0) {
        const timerId = window.setTimeout(() => {
          showNotification();
          renderScheduleList();
        }, delay);
        activeTimers.push(timerId);
      }
    });

    statusEl.textContent = 'Status: running';
    messageEl.textContent = `Scheduled ${scheduledDateTimes.length} reminder(s). Keep this page open.`;
  }

  function startReminder() {
    requestNotificationPermission();
    clearTimers();

    if (scheduleMode.value === 'hours') {
      scheduleHourlyReminder();
    } else if (scheduleMode.value === 'days') {
      scheduleDailyReminder();
    } else {
      scheduleDateTimeReminders();
    }
  }

  function stopReminder() {
    clearTimers();
    statusEl.textContent = 'Status: stopped';
    messageEl.textContent = 'Reminder stopped.';
  }

  scheduleMode.addEventListener('change', updateVisibleSettings);
  addDateTimeButton.addEventListener('click', addDateTimeReminder);
  startBtn.addEventListener('click', startReminder);
  stopBtn.addEventListener('click', stopReminder);

  setInitialDateTime();
  updateVisibleSettings();
}
