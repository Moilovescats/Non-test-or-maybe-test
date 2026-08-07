from http.server import BaseHTTPRequestHandler, HTTPServer
import os


def build_page(path):
    if path in {"/", "/index.html"}:
        return """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>StretchItOut</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: radial-gradient(circle at top, #fef3c7 0%, #bfdbfe 45%, #1d4ed8 100%);
      color: #111827;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }
    .card {
      background: linear-gradient(135deg, #ffffff, #f8fafc);
      padding: 2.5rem;
      border-radius: 24px;
      box-shadow: 0 16px 40px rgba(15, 23, 42, 0.2);
      max-width: 520px;
      width: 90%;
      border: 2px solid #bfdbfe;
      position: relative;
      z-index: 1;
    }
    .title-box {
      position: absolute;
      top: 0;
      left: 0;
      z-index: 3;
      background: #ffffff;
      padding: 0.5rem 0.9rem;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.12);
      border-bottom-right-radius: 12px;
    }
    .title-box h1 {
      margin: 0;
      font-size: 1.05rem;
      color: #111827;
      letter-spacing: 0.02em;
      text-transform: none;
      font-weight: 800;
    }
    h1 {
      margin: 0;
      font-size: 2.4rem;
      color: #f59e0b;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-shadow: 0 3px 10px rgba(245, 158, 11, 0.35);
      font-weight: 900;
    }
    .button-row {
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-top: 1.5rem;
      flex-wrap: wrap;
    }
    #home-intro {
      display: inline-block;
      padding: 0.85rem 1.1rem;
      border-radius: 8px;
      background: rgba(255,255,255,0.97);
      border: none;
      box-shadow: 0 10px 28px rgba(37,99,235,0.14);
      font-weight: 800;
      color: #0f172a;
      font-size: 1.15rem;
      letter-spacing: 0.01em;
    }
    .button {
      padding: 0.95rem 1.4rem;
      border: none;
      border-radius: 999px;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: white;
      font-size: 1rem;
      font-weight: bold;
      cursor: pointer;
      text-decoration: none;
      display: inline-block;
      box-shadow: 0 8px 20px rgba(37, 99, 235, 0.25);
      transition: transform 0.2s ease;
    }
    .button:hover {
      background: linear-gradient(135deg, #1d4ed8, #1e40af);
      transform: translateY(-2px);
    }
  </style>
</head>
<body>
  <div class=\"title-box\"><h1>StretchItOut</h1></div>
  <div class=\"card\">
      <p id=\"home-intro\">Choose what you want to explore.</p>
    <div class=\"button-row\">
      <a class=\"button\" href=\"/stretches\">Stretches</a>
      <a class=\"button\" href=\"/alarms\">Alarm</a>
    </div>
  </div>
</body>
</html>"""
    

    if path == "/stretches":
        return """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Stretches</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: radial-gradient(circle at top left, #fef3c7 0%, #bfdbfe 45%, #1d4ed8 100%);
      color: #111827;
      min-height: 100vh;
      padding: 2rem 1rem;
      box-sizing: border-box;
    }
    .card {
      background: linear-gradient(135deg, #ffffff, #f8fafc);
      padding: 2rem;
      border-radius: 24px;
      box-shadow: 0 16px 40px rgba(15, 23, 42, 0.2);
      width: 100%;
      max-width: 760px;
      margin: 0 auto;
      border: 2px solid #bfdbfe;
    }
    h1 {
      margin-top: 0;
      color: #1d4ed8;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .intro {
      color: #4b5563;
      margin-bottom: 1.25rem;
    }
    .filters {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }
    .filter-pill {
      padding: 0.55rem 0.9rem;
      border-radius: 999px;
      border: 1px solid #cbd5e1;
      background: #eff6ff;
      color: #1d4ed8;
      cursor: pointer;
      font-weight: 600;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.08);
    }
    .filter-pill.active {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: white;
      border-color: #2563eb;
      box-shadow: 0 8px 18px rgba(37, 99, 235, 0.2);
    }
    .stretch-list {
      display: grid;
      gap: 1rem;
      margin-top: 1rem;
    }
    .stretch-card {
      border: 1px solid #dbeafe;
      border-radius: 16px;
      padding: 1rem;
      background: linear-gradient(135deg, #f8fbff, #f9fafb);
      box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
    }
    .stretch-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.4rem;
    }
    .stretch-title {
      font-size: 1.05rem;
      font-weight: 700;
    }
    .tag {
      display: inline-block;
      padding: 0.3rem 0.6rem;
      border-radius: 999px;
      background: #dbeafe;
      color: #1d4ed8;
      font-size: 0.8rem;
      font-weight: 700;
      margin-right: 0.4rem;
    }
    .rating-row {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      margin-top: 0.8rem;
    }
    .rating-inputs {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }
    .rating-row input[type="number"] {
      width: 90px;
      padding: 0.45rem 0.6rem;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
    }
    .rating-row textarea {
      width: 100%;
      min-height: 70px;
      padding: 0.6rem 0.7rem;
      border-radius: 10px;
      border: 1px solid #cbd5e1;
      resize: vertical;
      box-sizing: border-box;
    }
    .rating-row button {
      padding: 0.55rem 0.8rem;
      border: none;
      border-radius: 999px;
      background: #2563eb;
      color: white;
      font-weight: 600;
      cursor: pointer;
    }
    .rating-row button:hover {
      background: #1d4ed8;
    }
    .rating-note {
      color: #6b7280;
      font-size: 0.95rem;
    }
    .saved-review {
      margin-top: 0.6rem;
      padding: 0.7rem 0.8rem;
      border-radius: 10px;
      background: #f3f4f6;
      color: #374151;
      border: 1px solid #e5e7eb;
      font-size: 0.95rem;
    }
    .how-to {
      margin-top: 0.7rem;
      padding: 0.8rem 0.9rem;
      border-radius: 12px;
      background: #dbeafe;
      color: #1e3a8a;
      font-size: 0.95rem;
      line-height: 1.5;
      border: 1px solid #93c5fd;
      font-weight: 600;
    }
    .link {
      display: inline-block;
      margin-top: 1rem;
      color: #2563eb;
      text-decoration: none;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>Stretches</h1>
    <p class=\"intro\">Stretch suggestions for different moods, energy levels, and comfort preferences. Tailor this list to your preferences and rate each one so others can see what worked for you.</p>
    <div class=\"filters\" aria-label=\"Stretch preference filters\">
      <button class=\"filter-pill active\" data-filter=\"all\">All</button>
      <button class=\"filter-pill\" data-filter=\"Gentle\">Gentle</button>
      <button class=\"filter-pill\" data-filter=\"Desk\">Desk</button>
      <button class=\"filter-pill\" data-filter=\"Quick\">Quick</button>      <button class="filter-pill" data-filter="Home">Home</button>
      <button class="filter-pill" data-filter="At desk">At desk</button>    </div>
    <div class=\"stretch-list\">
      <div class=\"stretch-card\" data-category=\"Gentle\">
        <div class=\"stretch-header\">
          <span class=\"stretch-title\">Shoulder rolls</span>
          <span class=\"tag\">Gentle</span>
        </div>
        <p>Easy shoulder circles that help loosen up after long work sessions.</p>        <div class="how-to">How to do it: Sit or stand tall, roll your shoulders forward slowly 5 times, then backward 5 times.</div>        <div class=\"rating-row\">
          <label for=\"rating-shoulders\">Rate this stretch</label>
          <div class="rating-inputs">
            <input id="rating-shoulders" type="number" min="1" max="5" step="1" value="5">
            <button type="button" data-save-target="rating-shoulders" data-note-target="note-shoulders">Save review</button>
          </div>
          <textarea id="note-shoulders" placeholder="Tell us why it felt great, or why it didn't work for you"></textarea>
          <div class="saved-review" id="saved-shoulders">No review saved yet.</div>
        </div>
      </div>
      <div class=\"stretch-card\" data-category=\"Desk\">
        <div class=\"stretch-header\">
          <span class=\"stretch-title\">Seated spinal twist</span>
          <span class=\"tag\">Desk</span>
        </div>
        <p>A simple seated twist to ease tension while you stay at your desk.</p>        <div class="how-to">How to do it: Sit upright, place one hand on the opposite knee, and gently rotate your torso without forcing the movement.</div>        <div class=\"rating-row\">
          <label for=\"rating-twist\">Rate this stretch</label>
          <div class="rating-inputs">
            <input id="rating-twist" type="number" min="1" max="5" step="1" value="5">
            <button type="button" data-save-target="rating-twist" data-note-target="note-twist">Save review</button>
          </div>
          <textarea id="note-twist" placeholder="Tell us why it felt great, or why it didn't work for you"></textarea>
          <div class="saved-review" id="saved-twist">No review saved yet.</div>
        </div>
      </div>
      <div class=\"stretch-card\" data-category=\"Quick\">
        <div class=\"stretch-header\">
          <span class=\"stretch-title\">Standing calf stretch</span>
          <span class=\"tag\">Quick</span>
        </div>
        <p>Fast, focused calf work that fits into a busy schedule.</p>        <div class="how-to">How to do it: Step one foot back, press the heel down, and hold for 15 to 20 seconds before switching sides.</div>        <div class=\"rating-row\">
          <label for=\"rating-calf\">Rate this stretch</label>
          <div class="rating-inputs">
            <input id="rating-calf" type="number" min="1" max="5" step="1" value="5">
            <button type="button" data-save-target="rating-calf" data-note-target="note-calf">Save review</button>
          </div>
          <textarea id="note-calf" placeholder="Tell us why it felt great, or why it didn't work for you"></textarea>
          <div class="saved-review" id="saved-calf">No review saved yet.</div>
        </div>
      </div>      <div class="stretch-card" data-category="Home">
        <div class="stretch-header">
          <span class="stretch-title">Child's pose</span>
          <span class="tag">Home</span>
        </div>
        <p>A gentle floor stretch that helps release tension in your back and hips.</p>
        <div class="how-to">How to do it: Kneel, sit back on your heels, and reach your arms forward while keeping your breathing slow and easy.</div>
        <div class="rating-row">
          <label for="rating-child-pose">Rate this stretch</label>
          <div class="rating-inputs">
            <input id="rating-child-pose" type="number" min="1" max="5" step="1" value="5">
            <button type="button" data-save-target="rating-child-pose" data-note-target="note-child-pose">Save review</button>
          </div>
          <textarea id="note-child-pose" placeholder="Tell us why it felt great, or why it didn't work for you"></textarea>
          <div class="saved-review" id="saved-child-pose">No review saved yet.</div>
        </div>
      </div>
      <div class="stretch-card" data-category="Home">
        <div class="stretch-header">
          <span class="stretch-title">Hamstring stretch on the floor</span>
          <span class="tag">Home</span>
        </div>
        <p>Great for loosening the back of your legs after a long day of sitting.</p>
        <div class="how-to">How to do it: Lie on your back, lift one leg, and gently straighten it while keeping the other knee bent.</div>
        <div class="rating-row">
          <label for="rating-hamstring">Rate this stretch</label>
          <div class="rating-inputs">
            <input id="rating-hamstring" type="number" min="1" max="5" step="1" value="5">
            <button type="button" data-save-target="rating-hamstring" data-note-target="note-hamstring">Save review</button>
          </div>
          <textarea id="note-hamstring" placeholder="Tell us why it felt great, or why it didn't work for you"></textarea>
          <div class="saved-review" id="saved-hamstring">No review saved yet.</div>
        </div>
      </div>
      <div class="stretch-card" data-category="At desk">
        <div class="stretch-header">
          <span class="stretch-title">Neck stretch</span>
          <span class="tag">At desk</span>
        </div>
        <p>A simple side-to-side neck stretch that helps relieve desk-related tension.</p>
        <div class="how-to">How to do it: Tilt your head toward one shoulder, hold for 10 to 15 seconds, and switch sides slowly.</div>
        <div class="rating-row">
          <label for="rating-neck">Rate this stretch</label>
          <div class="rating-inputs">
            <input id="rating-neck" type="number" min="1" max="5" step="1" value="5">
            <button type="button" data-save-target="rating-neck" data-note-target="note-neck">Save review</button>
          </div>
          <textarea id="note-neck" placeholder="Tell us why it felt great, or why it didn't work for you"></textarea>
          <div class="saved-review" id="saved-neck">No review saved yet.</div>
        </div>
      </div>
      <div class="stretch-card" data-category="At desk">
        <div class="stretch-header">
          <span class="stretch-title">Wrist and forearm stretch</span>
          <span class="tag">At desk</span>
        </div>
        <p>Helpful for easing stiffness from typing and mouse use.</p>
        <div class="how-to">How to do it: Extend one arm forward, gently pull your fingers back, and hold for 10 seconds before switching hands.</div>
        <div class="rating-row">
          <label for="rating-wrist">Rate this stretch</label>
          <div class="rating-inputs">
            <input id="rating-wrist" type="number" min="1" max="5" step="1" value="5">
            <button type="button" data-save-target="rating-wrist" data-note-target="note-wrist">Save review</button>
          </div>
          <textarea id="note-wrist" placeholder="Tell us why it felt great, or why it didn't work for you"></textarea>
          <div class="saved-review" id="saved-wrist">No review saved yet.</div>
        </div>
      </div>    </div>
    <p><a class=\"link\" href=\"/\">Back home</a></p>
  </div>
  <script>
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
  </script>
</body>
</html>"""

    if path == "/alarms":
        return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stretch reminder</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: radial-gradient(circle at top, #fef3c7 0%, #bfdbfe 45%, #1d4ed8 100%);
      color: #111827;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .card {
      background: linear-gradient(135deg, #ffffff, #f8fafc);
      padding: 2.5rem;
      border-radius: 24px;
      box-shadow: 0 16px 40px rgba(15, 23, 42, 0.2);
      max-width: 600px;
      width: 92%;
      border: 2px solid #bfdbfe;
    }
    h1 {
      margin-top: 0;
      font-size: 2rem;
      color: #1d4ed8;
    }
    .intro {
      color: #374151;
      margin-bottom: 1rem;
      line-height: 1.5;
    }
    .form-row,
    .form-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-top: 1rem;
      align-items: center;
    }
    .form-row label,
    .form-grid label {
      min-width: 120px;
      color: #334155;
      font-weight: 600;
    }
    input,
    select {
      padding: 0.75rem 0.9rem;
      border: 1px solid #cbd5e1;
      border-radius: 0.75rem;
      font-size: 1rem;
      color: #0f172a;
      background: #ffffff;
      box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.04);
    }
    input[type="time"],
    input[type="date"] {
      width: 160px;
    }
    select {
      min-width: 200px;
      flex: 1;
    }
    .button-row {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem;
      margin-top: 1.5rem;
    }
    .button {
      padding: 0.95rem 1.4rem;
      border: none;
      border-radius: 999px;
      background: #2563eb;
      color: white;
      font-size: 1rem;
      font-weight: bold;
      cursor: pointer;
      box-shadow: 0 10px 24px rgba(37, 99, 235, 0.18);
      transition: transform 0.2s ease, background 0.2s ease;
    }
    .button.secondary {
      background: linear-gradient(135deg, #6b7280, #4b5563);
    }
    .button:hover {
      transform: translateY(-2px);
      background: linear-gradient(135deg, #1d4ed8, #1e40af);
    }
    .button.secondary:hover {
      background: linear-gradient(135deg, #4b5563, #374151);
    }
    .small-note {
      color: #475569;
      font-size: 0.95rem;
      margin-bottom: 0.6rem;
    }
    .schedule-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: 0.6rem;
    }
    .schedule-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.75rem;
      padding: 0.85rem 1rem;
      border-radius: 0.95rem;
      background: #f8fbff;
      border: 1px solid #cbd5e1;
      color: #0f172a;
      font-size: 0.95rem;
    }
    .schedule-item button {
      padding: 0.45rem 0.75rem;
      border: none;
      border-radius: 0.75rem;
      background: #ef4444;
      color: white;
      cursor: pointer;
      font-size: 0.9rem;
    }
    .schedule-item button:hover {
      background: #dc2626;
    }
    .status {
      margin-top: 1.25rem;
      font-weight: bold;
      color: #334155;
    }
    .message {
      margin-top: 0.75rem;
      color: #1d4ed8;
      min-height: 1.5rem;
    }
    .link {
      display: inline-block;
      margin-top: 1.25rem;
      color: #2563eb;
      text-decoration: none;
      font-weight: 700;
    }
    .hidden {
      display: none;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Stretch reminder</h1>
    <p class="intro">Pick how often you want to get reminders and keep the page open. Notifications will fire in the browser while this tab is active.</p>

    <div class="form-row">
      <label for="scheduleMode">Reminder type</label>
      <select id="scheduleMode">
        <option value="hours">Every N hours</option>
        <option value="days">Every N days at time</option>
        <option value="datetime">Specific date/time</option>
      </select>
    </div>

    <div id="hoursSettings" class="form-row">
      <label for="hours">Repeat every</label>
      <input id="hours" type="number" min="1" value="1">
      <span>hour(s)</span>
    </div>

    <div id="daysSettings" class="form-row hidden">
      <label for="days">Repeat every</label>
      <input id="days" type="number" min="1" value="1">
      <span>day(s) at</span>
      <input id="dayTime" type="time" value="09:00">
    </div>

    <div id="dateTimeSettings" class="form-row hidden" style="flex-direction: column; align-items: stretch; gap: 1rem;">
      <div class="form-row" style="gap: 0.75rem;">
        <label for="reminderDate">Date</label>
        <input id="reminderDate" type="date">
      </div>
      <div class="form-row" style="gap: 0.75rem;">
        <label for="reminderTime">Time</label>
        <input id="reminderTime" type="time">
      </div>
      <button id="addDateTime" class="button secondary" type="button">Add date/time reminder</button>
      <div>
        <p class="small-note">Added reminders:</p>
        <ul id="scheduleList" class="schedule-list"></ul>
      </div>
    </div>

    <div class="form-row" style="margin-top: 1.25rem; gap: 0.75rem;">
      <label for="title">Notification title</label>
      <input id="title" type="text" value="Time to stretch" maxlength="40">
    </div>

    <div class="form-row switch-row">
      <input id="softSound" type="checkbox">
      <label for="softSound">Soft sound</label>
    </div>

    <div class="button-row">
      <button id="startBtn" class="button" type="button">Start reminder</button>
      <button id="stopBtn" class="button secondary" type="button">Stop reminder</button>
    </div>

    <p id="status" class="status">Status: idle</p>
    <p id="message" class="message">Choose a schedule and start your stretch reminder.</p>
    <a class="link" href="/">Back home</a>
  </div>

  <script>
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
      const dateValue = now.toISOString().slice(0, 10);
      const timeValue = now.toTimeString().slice(0, 5);
      reminderDateInput.value = dateValue;
      reminderTimeInput.value = timeValue;
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
        item.appendChild(label);
        item.appendChild(remove);
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
  </script>
</body>
</html>"""

    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Not found</title>
</head>
<body>
  <h1>Page not found</h1>
  <p><a href="/">Go home</a></p>
</body>
</html>"""


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path not in {"/", "/index.html", "/alarms", "/stretches"}:
            self.send_error(404, "Not Found")
            return

        html = build_page(path)
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def main():
    requested_port = int(os.environ.get("PORT", "8000"))
    port = requested_port
    while True:
        try:
            server = HTTPServer(("0.0.0.0", port), AppHandler)
            break
        except OSError as exc:
            if exc.errno != 98 or port >= requested_port + 10:
                raise
            port += 1

    print(f"Serving StretchItOut on http://0.0.0.0:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
