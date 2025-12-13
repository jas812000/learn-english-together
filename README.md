# Learn-English-Together

![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployed-success)
![Live Demo](https://img.shields.io/badge/Live%20Demo-Available-blue)

**Live Site:** https://jas812000.github.io/Learn-English-Together/  
**Repository:** https://github.com/jas812000/Learn-English-Together

---

## Project Overview

Learn-English-Together is a browser-based, audio-visual vocabulary learning platform designed for Thai speakers learning English. The system organizes vocabulary into hierarchical categories (e.g., House → Kitchen → Appliances) and presents each item using a combination of image, English label, and audio pronunciation. The platform emphasizes intuitive navigation, minimal text dependency, and immediate auditory feedback, making it suitable for early-stage and low-literacy learners.

The application is fully client-side and deployed via GitHub Pages, requiring no backend services or databases.

---

## Objective

The primary engineering goals of this project were to:

- Design an intuitive and accessible UI for beginner English learners
- Implement a scalable frontend structure for organizing large sets of static assets
- Provide reliable audio playback for pronunciation practice
- Support multilingual navigation cues (Thai and English)
- Optimize performance and simplicity using a static-site architecture

---

## Scope & Assumptions

- The project focuses on vocabulary recognition and pronunciation, not grammar or sentence construction
- Target users are Thai learners at beginner to A1 English proficiency
- All images and audio files are served as static assets
- No user accounts, progress tracking, or backend services are included
- The interface is designed to be mobile-friendly and touch-accessible

---

## Methodology / Approach

### UI/UX Design
- Hierarchical navigation to reduce cognitive load
- Large, clear imagery to support visual learning
- Speaker icons for intuitive audio playback
- Minimal English text to lower the entry barrier
- Thai-language category labels for orientation
- Consistent card-based layouts across categories

### Frontend Architecture
- Static HTML pages per category for predictable routing
- Organized directory structure for images and audio assets
- Lightweight JavaScript for handling audio playback
- Reusable layout patterns to support future expansion
- Deployment through GitHub Pages for fast, global access

---

## Tools & Technologies

- **Languages:** HTML5, CSS3, JavaScript
- **Architecture:** Static site, client-side only
- **Version Control:** Git, GitHub
- **Deployment:** GitHub Pages
- **Assets:** Local image and MP3 audio files

---

## Key Design Decisions

- **Static-site deployment** was chosen to maximize simplicity, performance, and reliability
- **Directory-based content organization** enables straightforward scaling by adding new categories
- **Native browser audio APIs** ensure compatibility and low latency
- **Minimalist UI design** aligns with ESL pedagogy and accessibility best practices
- **Breadcrumb navigation** supports deep exploration without user disorientation

---

## Artifacts & Documentation

- **Live Deployed Site:**  
  https://jas812000.github.io/Learn-English-Together/

- **Source Code Repository:**  
  https://github.com/jas812000/Learn-English-Together

---

## Outcome / Takeaways

This project demonstrates the ability to design and implement a user-centered frontend system with a clear pedagogical goal. It highlights strengths in UI/UX reasoning, frontend architecture, static-site deployment, and scalable asset organization. The system is intentionally lightweight, maintainable, and aligned with real-world ESL learning needs.

---

## License
© 2025 James Stevens. All rights reserved.

This source code is provided for educational, evaluation, and portfolio review purposes.
Permission is granted to clone and run the code locally for non-commercial review.

No permission is granted to copy, modify, redistribute, or use this code in
commercial or production systems without explicit written consent from the author.
