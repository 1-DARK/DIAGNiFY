# Diagnify - Medical Symptom Checker

## Overview

Diagnify is a web-based medical symptom checker application that helps users identify potential health conditions based on body part selection or symptom search. The application provides:

- Interactive human body diagrams (front and back views)
- Detailed information about possible medical conditions
- Recommended treatments and first aid advice
- Specialist doctor recommendations
- PDF report generation

## Files Structure

### HTML Files

1. **FrontSYM.html** - Front view of the human body with interactive symptom checker
2. **BackSYM.html** - Back view of the human body with interactive symptom checker

### CSS Files

1. **Feature.css** - Styling for feature cards and UI components
2. **Footer.css** - Styling for the footer section
3. **Navbar.css** - Styling for the navigation bar

### JavaScript Files

1. **Footer.js** - Functionality for the footer
2. **Navbar.js** - Functionality for the navigation bar

## Key Features

### Interactive Body Diagram
- Users can click on different body parts to see associated conditions
- Visual feedback with color changes on selection
- Responsive design works on mobile and desktop

### Comprehensive Medical Database
- Contains information on hundreds of conditions
- Organized by body part and system
- Includes:
  - Symptoms
  - Recommended medications
  - Severity levels
  - First aid instructions
  - Recommended specialists

### Search Functionality
- Search across all conditions and symptoms
- Real-time results as you type

### PDF Report Generation
- Create printable/downloadable reports
- Includes:
  - Selected body part
  - Possible conditions
  - Treatment recommendations
  - Specialist information

### Specialist Database
- Contains real doctor information including:
  - Names
  - Specialties
  - Hospital affiliations
  - Contact information
  - Addresses

## Technical Implementation

### Front-end Technologies
- HTML5
- CSS3 (with responsive design)
- JavaScript (ES6)
- jsPDF library for PDF generation
- Font Awesome for icons
- SVG for body diagrams

### Data Structure
- Medical conditions organized by body part
- Each condition includes:
  ```javascript
  {
    name: "Condition Name",
    symptoms: "Detailed symptoms",
    medications: "Recommended treatments",
    severity: "low/medium/high",
    specialist: "Recommended doctor type",
    firstAid: "Immediate care instructions"
  }
  ```

### Special Features
- Emergency protocols for critical conditions
- Severity level indicators (color-coded)
- Interactive UI with hover effects
- Cross-browser compatibility

## Usage Instructions

1. Open either FrontSYM.html or BackSYM.html in a web browser
2. Click on a body part or use the search function
3. View possible conditions and their details
4. Click "Download as PDF" to generate a report
5. Use the navigation menu to access other sections of the site

## Dependencies

- jsPDF (v2.5.1) - For PDF generation
- Font Awesome (v6.4.0) - For icons
- Google Fonts (Druk) - For typography

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (Chrome for Android, Safari for iOS)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Enhancements

- User accounts for saving history
- More detailed symptom questionnaires
- Integration with health APIs
- Multilingual support
- Dark/light mode toggle
