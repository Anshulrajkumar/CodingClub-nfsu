import urllib.request

base = "http://127.0.0.1:8765"
paths = [
    "/events.html",
    "/fund-my-crazy-event.html",
    "/hacking-event.html",
    "/assests/image/Google%20Gemini/Front_Image.jpg",
    "/assests/image/Google%20Gemini/e1.jpg",
    "/assests/image/Google%20Gemini/e2.jpg",
    "/assests/image/Google%20Gemini/e3.jpg",
]
for p in paths:
    try:
        with urllib.request.urlopen(base + p, timeout=5) as r:
            data = r.read()
            ctype = r.headers.get("Content-Type")
            print(f"{r.status} {p} ({len(data)} bytes) {ctype}")
    except Exception as e:
        print(f"FAIL {p}: {e}")

html = urllib.request.urlopen(base + "/events.html").read().decode("utf-8", "replace")
detail = urllib.request.urlopen(base + "/fund-my-crazy-event.html").read().decode("utf-8", "replace")
checks = [
    ("events has title", "Fund My Crazy" in html),
    ("events has date", "4 September, 2026" in html),
    ("events has 70", "70 students" in html),
    ("events has ambassadors", "Priyanshu Sahoo" in html and "Prasunma Das" in html),
    ("events has event 04", 'event-number">04' in html),
    ("events links detail page", "fund-my-crazy-event.html" in html),
    ("detail has gallery", "Event Gallery" in detail),
    ("detail has 70 stat", ">70<" in detail),
    ("detail has Code Sage", "Code Sage" in detail),
    ("hacking still 03", 'event-number">03' in html),
]
for name, ok in checks:
    print(("OK" if ok else "MISSING") + " - " + name)
