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
      background: linear-gradient(135deg, #fef3c7, #bfdbfe);
      color: #111827;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .card {
      background: white;
      padding: 2.5rem;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.12);
      text-align: center;
      max-width: 500px;
      width: 90%;
    }
    h1 {
      margin-top: 0;
      font-size: 2rem;
      color: #1d4ed8;
    }
    .button-row {
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-top: 1.5rem;
      flex-wrap: wrap;
    }
    .button {
      padding: 0.9rem 1.4rem;
      border: none;
      border-radius: 999px;
      background: #2563eb;
      color: white;
      font-size: 1rem;
      font-weight: bold;
      cursor: pointer;
      text-decoration: none;
      display: inline-block;
    }
    .button:hover {
      background: #1d4ed8;
    }
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>StretchItOut</h1>
    <p>Choose what you want to explore.</p>
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
      background: linear-gradient(135deg, #fef3c7, #bfdbfe);
      color: #111827;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .card {
      background: white;
      padding: 2.5rem;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.12);
      width: 90%;
      max-width: 600px;
    }
    .link {
      color: #2563eb;
      text-decoration: none;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>Stretches</h1>
    <p>This page is intentionally blank for now.</p>
    <p><a class=\"link\" href=\"/\">Back home</a></p>
  </div>
</body>
</html>"""

    if path == "/alarms":
        return """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Stretch reminder</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #fef3c7, #bfdbfe);
      color: #111827;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .card {
      background: white;
      padding: 2.5rem;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.12);
      text-align: center;
      max-width: 520px;
      width: 90%;
    }
    h1 {
      margin-top: 0;
      font-size: 2rem;
      color: #1d4ed8;
    }
    .controls {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 0.75rem;
      margin: 1.25rem 0;
      flex-wrap: wrap;
    }
    .switch-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      margin-top: 0.5rem;
      color: #374151;
    }
    .control-group {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    input, select {
      padding: 0.7rem;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      font-size: 1rem;
    }
    input {
      width: 90px;
    }
    select {
      min-width: 160px;
    }
    .button-row {
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-top: 1rem;
      flex-wrap: wrap;
    }
    .button {
      padding: 0.9rem 1.4rem;
      border: none;
      border-radius: 999px;
      background: #2563eb;
      color: white;
      font-size: 1rem;
      font-weight: bold;
      cursor: pointer;
      text-decoration: none;
      display: inline-block;
    }
    .button.secondary {
      background: #6b7280;
    }
    .button:hover {
      background: #1d4ed8;
    }
    .button.secondary:hover {
      background: #4b5563;
    }
    .status {
      margin-top: 1rem;
      font-weight: bold;
      color: #374151;
    }
    .message {
      margin-top: 0.75rem;
      color: #1d4ed8;
      min-height: 1.5rem;
    }
    .link {
      display: inline-block;
      margin-top: 1rem;
      color: #2563eb;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>Stretch reminder</h1>
    <p>Set a custom reminder so you never forget to stand up and stretch.</p>
    <div class=\"controls\">
      <div class=\"control-group\">
        <label for=\"hours\">Every</label>
        <input id=\"hours\" type=\"number\" min=\"1\" step=\"1\" value=\"1\">
        <span>hours</span>
      </div>
      <div class=\"control-group\">
        <label for=\"schedule\">Schedule</label>
        <select id=\"schedule\">
          <option value=\"daily\">Daily</option>
          <option value=\"every-other-day\">Every other day</option>
          <option value=\"every-week\">Every week</option>
        </select>
      </div>
    </div>
    <div class=\"controls\">
      <div class=\"control-group\">
        <label for=\"title\">Notification title</label>
        <input id=\"title\" type=\"text\" value=\"Time to stretch\" maxlength=\"40\">
      </div>
    </div>
    <div class=\"switch-row\">
      <input id=\"softSound\" type=\"checkbox\">
      <label for=\"softSound\">Soft sound</label>
    </div>
    <div class=\"button-row\">
      <button id=\"startBtn\" class=\"button\">Start reminder</button>
      <button id=\"stopBtn\" class=\"button secondary\">Stop reminder</button>
    </div>
    <p id=\"status\" class=\"status\">Status: idle</p>
    <p id=\"message\" class=\"message\">Choose a time and start your stretch reminder.</p>
    <a class=\"link\" href=\"/\">Back home</a>
  </div>
  <script>
    let timer = null;
    const hoursInput = document.getElementById('hours');
    const scheduleInput = document.getElementById('schedule');
    const titleInput = document.getElementById('title');
    const softSoundInput = document.getElementById('softSound');
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const statusEl = document.getElementById('status');
    const messageEl = document.getElementById('message');

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

    function showStretchAlert() {
      const title = titleInput.value.trim() || 'Time to stretch';
      const body = 'Stand up, roll your shoulders, and take a few slow breaths.';
      if ('Notification' in window && Notification.permission === 'granted') {
        new Notification(title, { body, tag: 'stretch-reminder' });
      } else {
        window.alert(`${title}\n${body}`);
      }
      playSoftSound();
      messageEl.textContent = `${title}: ${body}`;
      statusEl.textContent = 'Status: reminder triggered';
    }

    function stopReminder() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
      statusEl.textContent = 'Status: stopped';
      messageEl.textContent = 'Reminder stopped.';
    }

    function getScheduleLabel() {
      const hours = Math.max(1, Number(hoursInput.value) || 1);
      const schedule = scheduleInput.value;
      if (schedule === 'daily') {
        return `Daily reminder every ${hours} hour${hours === 1 ? '' : 's'}.`;
      }
      if (schedule === 'every-other-day') {
        return `Reminder every other day, every ${hours} hour${hours === 1 ? '' : 's'}.`;
      }
      return `Reminder every week, every ${hours} hour${hours === 1 ? '' : 's'}.`;
    }

    startBtn.addEventListener('click', () => {
      const hours = Math.max(1, Number(hoursInput.value) || 1);
      if ('Notification' in window && Notification.permission === 'default') {
        Notification.requestPermission().catch(() => {});
      }
      stopReminder();
      timer = window.setInterval(showStretchAlert, hours * 60 * 60 * 1000);
      statusEl.textContent = 'Status: running';
      messageEl.textContent = getScheduleLabel();
    });

    stopBtn.addEventListener('click', stopReminder);
  </script>
</body>
</html>"""

    return """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Not found</title>
</head>
<body>
  <h1>Page not found</h1>
  <p><a href=\"/\">Go home</a></p>
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
