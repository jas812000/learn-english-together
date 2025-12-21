# English Practice Zone (Learn English Together)

## Overview
English Practice Zone is a lightweight, browser-based vocabulary practice application designed for Thai speakers learning English.

The project emphasizes clarity, repetition, and low-friction interaction by combining images, English labels, and tap-to-play pronunciation audio. It is implemented as a static web application to keep deployment simple, portable, and easy to understand.

The current version focuses on a small, complete feature set rather than breadth. Only fully working categories are exposed to users.

---

## Features
- Image-based vocabulary cards
- Tap-to-play pronunciation audio
- Bilingual category navigation (Thai and English)
- Mobile-friendly card layout
- Static-site architecture (no backend required)

---

## Architecture Overview
The application follows a simple, static, content-driven structure:

### Application Layer
- index.html serves as the entry point and category selector
- Each category page renders vocabulary cards for a specific topic

### Presentation Layer
- HTML defines page structure and semantic content
- CSS provides responsive layout and consistent visual styling

### Interaction Layer
Vanilla JavaScript handles:
- Audio playback
- Small UI interactions
- No frameworks or build tools are required

### Asset Organization
Each vocabulary set contains:
- image/ directory for PNG images
- audio/ directory for MP3 pronunciation files
This keeps content self-contained and easy to extend

### Data Model
Vocabulary items are defined directly in page-level JavaScript as small, explicit data structures.

Each item includes:
- An identifier
- A display label
- An image file reference
- An audio file reference

This approach favors transparency and ease of modification over abstraction.

---

## Error Handling Strategy
The application uses defensive interaction patterns, including:

- Safe handling of missing audio elements
- Graceful failure when media playback is blocked by the browser
- No hard dependency on external services or APIs

Failures in individual media files do not prevent the rest of the page from functioning.

---

## Running the Application
The project is a static site and does not require a backend or build step.

Run locally using Python:
```bash
python3 -m http.server 8000
```

Then open in a browser:
Home page:
```bash
http://localhost:8000
```
Example pages:
```bash
http://localhost:8000/Numbers/SingleDigits/
```
```bash
http://localhost:8000/House/
```

Using a local server avoids browser restrictions associated with opening HTML files directly from disk.

---

## Getting Started
### Prerequisites
A modern web browser
Python 3 (for local development server)

### Run the application
```bash
python3 -m http.server 8000
```

---

## Project Structure
- index.html — homepage and category navigation
- assets/ — shared CSS and JavaScript
- Numbers/ — number-related vocabulary sets
- House/ — house-related vocabulary sets
Each vocabulary set includes image/ and audio/ subdirectories

---

## Testing
This project currently relies on manual browser-based testing.

Planned improvements include:
Basic smoke tests to ensure pages load correctly
Automated checks to verify asset paths and media availability

---

## What This Project Demonstrates
- Clear organization of static web projects
- User-focused design for language learning
- Practical handling of media assets
- Progressive scope control (shipping complete features first)
- Clean repository hygiene suitable for portfolio review

---

## License
This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
