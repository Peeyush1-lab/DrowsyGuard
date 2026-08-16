# DrowsyGuard

### Real-Time AI Drowsiness Detection & Alert System

DrowsyGuard is a modular, real-time computer vision system designed to detect driver drowsiness and trigger an alert when signs of fatigue are detected.

The project is being developed incrementally with a focus on modular architecture, testability, error handling, and scalability.

> 🚧 **Status:** Active Development

---

## 🎯 Project Objective

Driver fatigue is a major safety concern, particularly during long-distance and night-time driving.

DrowsyGuard aims to provide a software-based monitoring system that:

- Captures real-time video from a camera
- Detects and tracks a driver's face
- Analyzes eye and facial characteristics
- Estimates drowsiness
- Triggers an audible warning
- Records monitoring sessions and relevant metrics

The final system is intended to operate as a continuous real-time monitoring pipeline.

---

## 🏗️ Current Architecture

The project follows a modular `src`-based Python architecture.

```text
DrowsyGuard/
│
├── src/
│   └── drowsyguard/
│       ├── __init__.py
│       ├── alarm.py
│       └── camera.py
│
├── tests/
│   ├── test_alarm.py
│   └── test_camera_manual.py
│
├── assets/
│   └── sounds/
│       └── alarm.mp3
│
├── data/
│
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
└── run.py
```

The architecture will expand as additional computer vision and monitoring components are implemented.

---

## 🚀 Development Pipeline

The intended DrowsyGuard pipeline is:

```text
Camera
   ↓
Video Frame
   ↓
Face Detection
   ↓
Eye Detection
   ↓
Drowsiness Analysis
   ↓
Alert Decision
   ↓
Alarm
   ↓
Session Logging
```

Each stage is being developed as an independent component so that the system can be tested and debugged incrementally.

---

## ✅ Implemented Features

### v0.1.0 — Project Foundation

- Initial project structure
- Git and GitHub repository setup
- Python virtual environment
- Dependency management
- Basic project documentation

### v0.2.0 — Alarm Engine

- Implemented reusable `Alarm` class
- Pygame-based audio playback
- Alarm start/stop functionality
- Volume control
- Manual alarm testing
- Audio asset integration

### v0.3.0 — Camera Capture

- OpenCV camera integration
- Reusable `Camera` class
- Camera initialization validation
- Real-time frame capture
- Frame validation
- Camera resource cleanup
- Camera error handling
- Manual camera testing
- Refactored project into a clean `src/drowsyguard` architecture
- Added `pyproject.toml` package configuration

---

## 🔨 Upcoming Milestones

### v0.4.0 — Face Detection

- Real-time face detection
- Face bounding box visualization
- Camera-to-detection pipeline
- Face detection testing

### v0.5.0 — Eye Detection

- Eye region detection
- Eye-state analysis
- Eye tracking preparation

### v0.6.0 — Drowsiness Detection

- Eye Aspect Ratio (EAR)
- Blink detection
- Prolonged eye closure detection
- Drowsiness scoring
- Detection thresholds

### v0.7.0 — Alert System

- Drowsiness-triggered alarm
- Alert cooldown
- Alert state management
- False-trigger reduction

### v0.8.0 — Session Tracking

- Monitoring sessions
- Drowsiness events
- Detection statistics
- Local data persistence

### v0.9.0 — Monitoring Dashboard

- Real-time monitoring interface
- Detection metrics
- Session summaries
- System status

### v1.0.0 — DrowsyGuard MVP

- Integrated real-time detection pipeline
- Camera
- Face detection
- Eye analysis
- Drowsiness detection
- Alert system
- Session tracking
- Monitoring dashboard

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Core development |
| OpenCV | Computer vision and camera processing |
| Pygame | Audio alert system |
| NumPy | Numerical and image-processing operations |
| Git | Version control |
| GitHub | Source control and project management |

Additional technologies will be introduced as the project evolves.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Peeyush1-lab/DrowsyGuard.git
cd DrowsyGuard
```

### 2. Create a virtual environment

Windows:

```powershell
py -3.13 -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the project

```powershell
python -m pip install -e .
```

Or install the listed dependencies:

```powershell
python -m pip install -r requirements.txt
```

---

## ▶️ Running the Current Modules

### Test the Alarm Engine

```powershell
python -m tests.test_alarm
```

### Test Camera Capture

```powershell
python -m tests.test_camera_manual
```

Press `Q` in the camera window to stop the camera.

---

## 🧪 Testing Philosophy

DrowsyGuard is being developed using incremental testing.

Each major component is tested independently before being integrated into the complete system.

Current manual tests include:

```text
Alarm Engine
     ↓
Camera Capture
     ↓
Future:
Face Detection
     ↓
Eye Detection
     ↓
Drowsiness Detection
```

This approach makes debugging easier because failures can be isolated to individual components.

Automated testing will be expanded as the project matures.

---

## 📌 Design Principles

DrowsyGuard is being developed around the following principles:

### Modularity

Each major system responsibility is separated into its own module.

### Testability

Components are tested independently before integration.

### Error Handling

Expected failures such as camera initialization and frame capture problems are handled explicitly.

### Scalability

The architecture is designed to allow additional detection, monitoring, storage, and interface components to be added without restructuring the entire application.

### Maintainability

The project uses a structured Python package layout and versioned development milestones.

---

## 🔖 Release History

| Version | Milestone | Status |
|---|---|---|
| v0.1.0 | Project Foundation | ✅ Complete |
| v0.2.0 | Alarm Engine | ✅ Complete |
| v0.3.0 | Camera Capture | ✅ Complete |
| v0.4.0 | Face Detection | 🚧 Planned |
| v0.5.0 | Eye Detection | 🚧 Planned |
| v0.6.0 | Drowsiness Detection | 🚧 Planned |
| v0.7.0 | Alert System | 🚧 Planned |
| v0.8.0 | Session Tracking | 🚧 Planned |
| v0.9.0 | Monitoring Dashboard | 🚧 Planned |
| v1.0.0 | DrowsyGuard MVP | 🚧 Planned |

---

## ⚠️ Current Limitations

DrowsyGuard is currently under active development.

The current implementation provides:

- Alarm functionality
- Camera capture
- Basic project architecture

The actual AI/computer-vision drowsiness detection pipeline has **not yet been implemented**.

Upcoming releases will add these capabilities incrementally.

---

## 🛣️ Roadmap

```text
Foundation
    │
    ▼
Alarm Engine
    │
    ▼
Camera Capture
    │
    ▼
Face Detection
    │
    ▼
Eye Detection
    │
    ▼
Drowsiness Analysis
    │
    ▼
Alert System
    │
    ▼
Session Tracking
    │
    ▼
Monitoring Dashboard
    │
    ▼
DrowsyGuard v1.0
```

---

## 👨‍💻 Author

**Peeyush Tiwari**

GitHub:  
https://github.com/Peeyush1-lab

---

## 📄 License

This project will be licensed before the v1.0.0 release.

---

> DrowsyGuard is an educational and engineering project focused on exploring real-time computer vision, modular Python architecture, and intelligent alert systems.
