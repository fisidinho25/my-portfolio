"""
Project data for the portfolio website.
Customize this file to add your own projects, descriptions, and technologies.
"""

PROJECTS = [
    {
        'id': 1,
        'title': 'Personal Website',
        'short_description': 'A responsive personal website built with HTML, CSS, and JavaScript.',
        'long_description': 'This project showcases my first venture into web development. Built with pure HTML5, CSS3, and vanilla JavaScript, it features a responsive design that works across all devices. The website includes smooth scrolling navigation, animated elements, and a contact form. I learned fundamental web development concepts including semantic HTML, CSS Grid and Flexbox, and DOM manipulation with JavaScript.',
        'technologies': ['HTML5', 'CSS3', 'JavaScript', 'Responsive Design'],
        'image_url': 'https://pixabay.com/get/g044fa49bc01c5804f816e5041dfc61d8ec9a6ea54d5e9d3b31ef810e8f9590b428c88188f0810dfef1912faf05d2671f676edf0ba26c67968ca313ad9d0b866f_1280.png',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Web Development'
    },
    {
        'id': 2,
        'title': 'Todo List App',
        'short_description': 'A simple todo list application with local storage functionality.',
        'long_description': 'An interactive todo list application that allows users to add, edit, delete, and mark tasks as complete. The app uses local storage to persist data between browser sessions. Features include task filtering (all, active, completed), drag-and-drop reordering, and a clean, intuitive interface. This project taught me about event handling, local storage APIs, and creating dynamic user interfaces.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Local Storage'],
        'image_url': 'https://pixabay.com/get/g1ddc0a08f9fc38c3a539213ce01bcadaee733e7145c91450ae2123cf3d345b1cac44bc07edf56c4bddda79ee500da89bcfbc235bb79644bebcc423e99fe9e634_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Web Application'
    },
    {
        'id': 3,
        'title': 'Weather App',
        'short_description': 'A weather application that fetches data from a weather API.',
        'long_description': 'A beautiful weather application that displays current weather conditions and 5-day forecasts. Users can search for weather by city name or use geolocation for their current location. The app features weather icons, temperature conversion between Celsius and Fahrenheit, and detailed weather information including humidity, wind speed, and UV index. This project introduced me to API integration, asynchronous JavaScript, and working with JSON data.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Weather API', 'Geolocation'],
        'image_url': 'https://pixabay.com/get/gf99375c9816e57aa3b171980167c5ace8b30ebca456c313233901cfe37f570194ae42b539b2bc7a824594b3eb17864bf706a98592f89c2f031a4771b58270c63_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'API Integration'
    },
    {
        'id': 4,
        'title': 'Calculator',
        'short_description': 'A functional calculator with basic arithmetic operations.',
        'long_description': 'A fully functional calculator application with a sleek design inspired by modern mobile calculators. Features include basic arithmetic operations (addition, subtraction, multiplication, division), decimal support, keyboard input support, and error handling for edge cases like division by zero. The calculator includes memory functions and a history feature. This project strengthened my understanding of JavaScript functions, event handling, and user interface design.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Math Functions'],
        'image_url': 'https://pixabay.com/get/gb9dc65087f057b6aa2d39930a6ef6de24aa7ae04922f022ca583394fe9fc5ae58aa35adaf10b98c7fdb93eda35cf4e82044ee0b6bff0cc87988bb4ed2504035b_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Utility Application'
    },
    {
        'id': 5,
        'title': 'Random Quote Generator',
        'short_description': 'A quote generator that displays inspirational quotes with sharing features.',
        'long_description': 'An inspirational quote generator that fetches quotes from various categories including motivation, success, wisdom, and life. Features include random quote generation, category filtering, favorite quotes functionality, and social media sharing buttons. The app has a beautiful gradient background that changes with each quote and includes smooth animations. This project taught me about API consumption, array manipulation, and creating engaging user experiences.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Quotes API', 'Social Sharing'],
        'image_url': 'https://pixabay.com/get/g276a602bc32ec8923864a9951f034cc060805aeadeab6016f9f389a568f59ab0188d3eca0ae86c2831cf7b2d09b7e7069aae7dac25b9cbea908e6037b372332b_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Content Application'
    },
    {
        'id': 6,
        'title': 'Color Palette Generator',
        'short_description': 'A tool for generating and saving beautiful color palettes.',
        'long_description': 'A creative tool for designers and developers to generate, customize, and save color palettes. Features include random palette generation, color harmony rules (complementary, triadic, analogous), HSL adjustments, hex/RGB/HSL color format conversion, and palette export functionality. Users can lock colors they like while generating new combinations for the rest. This project enhanced my understanding of color theory, CSS custom properties, and browser storage APIs.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Color Theory', 'Canvas API'],
        'image_url': 'https://pixabay.com/get/g523dd601c5db7a9e4f94c363fd68bee26b3c304ab6ac71a8b1a4c98578a76557819cd10e009c3072a70e07fc20876f2887dcce9a2ea0370e51ab92f7e49b6045_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Design Tool'
    },
    {
        'id': 7,
        'title': 'Memory Card Game',
        'short_description': 'A classic memory matching game with multiple difficulty levels.',
        'long_description': 'An entertaining memory card game where players flip cards to find matching pairs. The game includes multiple difficulty levels (4x4, 6x6, 8x8 grids), a timer, move counter, high score tracking, and themed card sets (animals, emojis, symbols). Features smooth flip animations, sound effects, and a celebration animation when the game is completed. This project improved my skills in game logic, CSS animations, and state management.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Game Logic', 'Animations'],
        'image_url': 'https://pixabay.com/get/gf8f378b65d9d6371e67147cfdd24187daa9b04e0d8ff1c8355bc87dfe4acfb25bc0299a00a5cc5a84d833fdd0e01586ab747844f0d13f204321d000bc290df46_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Game Development'
    },
    {
        'id': 8,
        'title': 'Digital Clock',
        'short_description': 'A stylish digital clock with multiple time zones and themes.',
        'long_description': 'A beautiful digital clock application featuring real-time updates, multiple time zones, customizable themes (dark, light, neon), and various clock formats (12/24 hour, different date formats). The clock includes alarm functionality, stopwatch, and countdown timer features. Background changes based on time of day, creating an immersive experience. This project taught me about JavaScript Date objects, setInterval functions, and creating polished user interfaces.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Date/Time APIs', 'Responsive Design'],
        'image_url': 'https://pixabay.com/get/g67d3dee82e804591aa0294aa017e034a660cb4e4c3a9989cc72866059d209b7df342b6be2e9e096d71958e2a77e53c16f45242519377968cf3553f8e90e774a3_1280.png',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Utility Application'
    },
    {
        'id': 9,
        'title': 'Recipe Finder',
        'short_description': 'A recipe search application with ingredient-based filtering.',
        'long_description': 'A comprehensive recipe finder that allows users to search for recipes by ingredients, cuisine type, or dietary restrictions. Features include detailed recipe instructions, nutritional information, cooking time estimates, difficulty levels, and the ability to save favorite recipes. The app uses a recipe API to fetch thousands of recipes and includes advanced filtering options. This project expanded my knowledge of complex API integration and data filtering techniques.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Recipe API', 'Search Functionality'],
        'image_url': 'https://pixabay.com/get/g928124c76d490282829dcefc6e71bbb61556b2b110a1c90e3e6b279eaa0a05e1d3cc30983bc0f39f3115b68b059a4e05b9d0de839032ab1b1ad038030dbade09_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Lifestyle Application'
    },
    {
        'id': 10,
        'title': 'Password Generator',
        'short_description': 'A secure password generator with customizable options.',
        'long_description': 'A security-focused password generator that creates strong, customizable passwords. Users can specify password length, include/exclude character types (uppercase, lowercase, numbers, symbols), avoid ambiguous characters, and generate multiple passwords at once. The app includes password strength indicators, copy-to-clipboard functionality, and educational tips about password security. This project taught me about cryptographic security, random number generation, and user experience design for security tools.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Cryptography', 'Security'],
        'image_url': 'https://pixabay.com/get/g69c51d6e0a320eb6655a76cf1b2a4a3945772ce500bd0384f81ed91dd69da0a58275ddce1397585e26d7ca8be6d7a3a22a0613cf00b6ef0a193b8f387c0cf19b_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Security Tool'
    },
    {
        'id': 11,
        'title': 'QR Code Generator',
        'short_description': 'A QR code generator for text, URLs, and contact information.',
        'long_description': 'A versatile QR code generator that creates QR codes for various data types including text, URLs, email addresses, phone numbers, and contact information (vCard). Features include customizable QR code colors, size options, error correction levels, and the ability to download generated codes as PNG images. The app also includes a QR code reader using the device camera. This project introduced me to working with external libraries and camera APIs.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'QR Code Library', 'Camera API'],
        'image_url': 'https://pixabay.com/get/gc166e0b28c4b22e90bec0546955fed455af19791b73842ffd7a2bbf686e25bf2f0d18f75f224ec3cb0cdcb4a6bdac06f4966a68714366ebf514c9498ab154cfe_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Utility Tool'
    },
    {
        'id': 12,
        'title': 'Unit Converter',
        'short_description': 'A comprehensive unit conversion tool for various measurements.',
        'long_description': 'A complete unit conversion application supporting length, weight, temperature, volume, area, speed, and energy conversions. The app features an intuitive interface with real-time conversion as you type, conversion history, favorite conversions, and the ability to chain conversions. It includes common conversion shortcuts and educational information about different measurement systems. This project strengthened my understanding of mathematical calculations and creating reusable code modules.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Mathematical Calculations', 'Modular Code'],
        'image_url': 'https://pixabay.com/get/ga7b707751bb1af43a483066c9d8a8a1ac9e54e4fc456030b056191d1747294b2259bd5f6194efbc3d777c139a07931c3_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Utility Application'
    },
    {
        'id': 13,
        'title': 'Image Gallery',
        'short_description': 'A responsive image gallery with lightbox and filtering features.',
        'long_description': 'An elegant image gallery application with advanced features including lightbox viewing, image filtering by categories, search functionality, lazy loading for performance, and slideshow mode. The gallery supports multiple image formats and includes zoom, rotation, and fullscreen viewing options. Users can create custom albums and share individual images or entire galleries. This project taught me about image optimization, lazy loading techniques, and creating smooth user interactions.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Image Processing', 'Lazy Loading'],
        'image_url': 'https://pixabay.com/get/gb653fa3cac1a82a51bf5bba8fe7c2d0855366138f60928a4ead7a73670494c08904980277475a3f3b78160d6bb07a3e5e8916c4403810efdf2fe606615ada5bc_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Media Application'
    },
    {
        'id': 14,
        'title': 'Quiz Application',
        'short_description': 'An interactive quiz app with multiple categories and scoring.',
        'long_description': 'An engaging quiz application featuring multiple question categories (science, history, sports, entertainment), different difficulty levels, timed questions, and comprehensive scoring with detailed results. The app includes progress tracking, hints system, question explanation after each answer, and leaderboard functionality. Users can create custom quizzes and share them with others. This project enhanced my skills in data management, user interface design, and creating engaging interactive experiences.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Data Management', 'Interactive UI'],
        'image_url': 'https://pixabay.com/get/g76311c32fe442e51b6ee2ad77b92da6af52195c47313bb7541fdfbb2a4ad998d4643c0891c632466a433af76cb22011b6597878dcf902374f1533cd9050a9fc9_1280.jpg',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Educational Application'
    },
    {
        'id': 15,
        'title': 'Text Analyzer',
        'short_description': 'A comprehensive text analysis tool with various metrics and insights.',
        'long_description': 'A powerful text analysis tool that provides comprehensive insights into any text input. Features include word count, character count, reading time estimation, keyword density analysis, readability scores, sentiment analysis, and text statistics. The app can analyze multiple documents simultaneously and export detailed reports. It includes text formatting tools and supports multiple languages. This project deepened my understanding of string manipulation, regular expressions, and statistical analysis algorithms.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Text Processing', 'Statistical Analysis'],
        'image_url': 'https://pixabay.com/get/g24675963d8d041f83030fa6118399726e7520cb6bab038cf53951ed863fb5ad13deee1abf5510f6b70780580df9ce52282ed86f69ada5dee842c9ed5717322da_1280.png',
        'github_url': '#',
        'live_demo_url': '#',
        'category': 'Productivity Tool'
    }
]

# Skills data for the about/skills section
SKILLS = {
    'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'Bootstrap', 'Responsive Design', 'jQuery'],
    'Backend': ['Python', 'Flask', 'Django', 'SQL', 'REST APIs'],
    'Tools': ['Git', 'GitHub', 'VS Code', 'Chrome DevTools', 'Figma'],
    'Concepts': ['Web Development', 'UI/UX Design', 'Database Design', 'API Integration']
}

# Personal information - CUSTOMIZE THIS SECTION
PERSONAL_INFO = {
    'name': 'Fisayo Adedoyin',
    'title': 'Web Developer & Programming Enthusiast',
    'email': 'Adedoyinfisayo305@gmail.com',
    'phone': '+(234) 8078-9240-58',
    'location': 'Lagos, Nigeria',
    'linkedin': 'https://www.linkedin.com/in/fisayo-adedoyin-78086197/',
    'github': 'https://github.com/fisidinho25',
    'bio': '''Welcome to my portfolio! I'm a passionate web developer with a love for creating 
    clean, functional, and user-friendly applications. Through my journey in programming, 
    I've built these 15 projects that showcase my growth and skills in web development. 
    Each project represents a step forward in my learning process, from basic HTML/CSS 
    websites to more complex applications with APIs and interactive features.''',
    'experience_years': '3+',
    'projects_completed': '15+'
}