# Diagnify - Comprehensive Health & Wellness Platform

## Overview
Diagnify is an advanced health technology platform that combines AI-powered medical diagnostics with personalized wellness planning. The application integrates interactive symptom checkers, medical image analysis, and real-time health consultations with a comprehensive fitness and nutrition system.

## Key Features

### Medical Diagnostic Tools
- **Interactive Body Maps**:
  - Front and back views (FrontSYM.html, BackSYM.html)
  - Clickable body parts with condition information
  - Visual feedback with color-coded severity indicators
  - PDF report generation with jsPDF

- **AI Medical Imaging**:
  - X-ray, MRI, and scan analysis
  - Instant AI-generated insights
  - Confidence percentage indicators
  - Potential issue detection

### Wellness Planning
- **Personalized Fitness** (D.html):
  - Condition-specific exercise routines
  - Joint-friendly workouts
  - Progressive difficulty levels

- **Nutrition Planning** (Vision.html):
  - Anti-inflammatory meal plans
  - Culturally-sensitive dietary recommendations
  - Heart-healthy options

### Interactive Features
- **Video Chatbot**:
  - Real-time video consultations
  - AI health assistant
  - Text and video messaging capabilities

- **Search Functionality**:
  - Comprehensive medical database
  - Real-time symptom search
  - Emergency protocols for critical conditions

## Technical Implementation

### Core Technologies
- **Frontend**:
  - HTML5, CSS3, JavaScript (ES6)
  - Bootstrap 5.3.0 (responsive design)
  - GSAP 3.12.2 (animations)
  - Font Awesome 6.0 (icons)

- **Specialized Libraries**:
  - jsPDF (PDF report generation)
  - GSAP plugins (ScrollTrigger, SplitText)
  - SVG for interactive body diagrams

### Data Structure
```javascript
{
  bodyPart: "Head",
  conditions: [
    {
      name: "Migraine",
      symptoms: ["Throbbing pain", "Sensitivity to light"],
      medications: ["Ibuprofen", "Triptans"],
      severity: "medium",
      specialist: "Neurologist",
      firstAid: "Rest in dark room",
      fitness: ["Neck stretches", "Aerobic exercise"],
      nutrition: ["Magnesium-rich foods", "Hydration"]
    }
  ]
}
```

## File Structure
```
├── index.html            - Main application entry point
├── FrontSYM.html         - Front body view symptom checker
├── BackSYM.html          - Back body view symptom checker
├── D.html                - Fitness planner
├── Vision.html           - Nutrition model
├── css/
│   ├── Feature.css       - Feature card styling
│   ├── Footer.css        - Footer styling
│   └── Navbar.css        - Navigation styling
├── js/
│   ├── Footer.js         - Footer functionality
│   └── Navbar.js         - Navigation functionality
├── assets/
│   ├── Favi.png          - Application favicon
│   ├── img1-4.png/jpg    - Application images
│   └── body-diagrams/    - SVG body maps
```

## Usage Instructions

1. **Symptom Checking**:
   - Select FrontSYM.html or BackSYM.html
   - Click on body parts or search symptoms
   - View condition details and generate PDF reports

2. **Wellness Planning**:
   - Access D.html for fitness routines
   - Visit Vision.html for nutrition plans
   - Get personalized recommendations based on conditions

3. **AI Features**:
   - Upload medical images for analysis
   - Use the video chatbot for consultations
   - Receive instant diagnostic insights

## System Requirements

### Browser Support
- Chrome, Firefox, Safari, Edge (latest versions)
- Mobile browsers (iOS/Android)

### Responsive Design
- Desktop (≥1024px)
- Tablet (768-1024px)
- Mobile (<768px)

## License & Copyright
- Currently unlicensed
- All rights reserved by ACMECorp (2024)

## Roadmap & Future Enhancements

### Short-term
- User authentication system
- Dark/light mode toggle
- Enhanced emergency protocols

### Mid-term
- Health tracking device integration
- Expanded medical image analysis
- Multilingual support

### Long-term
- Telemedicine integration
- AI-powered diagnostic questionnaires
- Community health features

For support or inquiries, please contact the Diagnify development team.

---

This merged README combines both versions while:
1. Maintaining all key features from both
2. Organizing information logically
3. Including technical details
4. Providing clear usage instructions
5. Outlining future plans

The structure flows from overview to specific details, making it easy for both technical and non-technical users to understand the application's capabilities.

##License

- This project is licensed under the MIT License - see the LICENSE file for details.
