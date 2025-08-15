# Personal Portfolio Website

## Overview

This is a Flask-based personal portfolio website designed to showcase projects and provide a professional online presence. The application features a clean, responsive design with project galleries, contact functionality, and a modern user interface built with Bootstrap 5. The site is structured as a simple portfolio platform that can be easily customized with personal information and project details.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask for server-side rendering
- **CSS Framework**: Bootstrap 5 for responsive design and UI components
- **JavaScript**: Vanilla JavaScript for interactive features including smooth scrolling, animations, project filtering, and form handling
- **Styling**: Custom CSS with CSS variables for easy theming and Google Fonts (Inter) for typography
- **Layout Structure**: Base template with extending child templates for consistent navigation and footer across all pages

### Backend Architecture
- **Web Framework**: Flask with a simple MVC pattern
- **Application Structure**: Modular design with separate files for routes, models, and data
- **Session Management**: Flask sessions with configurable secret key
- **Proxy Support**: ProxyFix middleware for proper handling behind reverse proxies
- **Environment Configuration**: Environment variables for database URLs and session secrets

### Data Storage Solutions
- **Primary Database**: SQLite for development with SQLAlchemy ORM
- **Database Models**: Simple schema with ContactSubmission model for form data
- **Static Data**: Project information stored in Python data structures for easy management
- **Migration Strategy**: SQLAlchemy's create_all() for automatic table creation

### Content Management
- **Project Data**: Centralized project information in data/projects.py file
- **Static Assets**: Organized in static/ directory with separate CSS and JavaScript files
- **Image Handling**: External image URLs (Pixabay) for project thumbnails
- **Template Organization**: Hierarchical template structure with base template and page-specific templates

## External Dependencies

### Core Web Technologies
- **Flask**: Web application framework
- **SQLAlchemy**: Database ORM and toolkit
- **Werkzeug**: WSGI utility library for proxy handling

### Frontend Libraries
- **Bootstrap 5**: CSS framework from CDN for responsive design
- **Font Awesome**: Icon library from CDN
- **Google Fonts**: Typography (Inter font family)

### Development Tools
- **Python Logging**: Built-in logging for debugging and monitoring
- **Environment Variables**: Configuration management for database and session settings

### Database
- **SQLite**: File-based database for development (configurable via DATABASE_URL environment variable)
- **Database Pooling**: Connection pool management with recycle and pre-ping options

### Hosting Considerations
- **Static File Serving**: Flask's built-in static file serving
- **Port Configuration**: Configurable host and port binding (default: 0.0.0.0:5000)
- **Debug Mode**: Configurable debug setting for development vs production