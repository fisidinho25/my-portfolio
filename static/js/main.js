/**
 * Main JavaScript file for Portfolio Website
 * Contains interactive functionality and animations
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all components
    initSmoothScrolling();
    initAnimations();
    initNavbar();
    initProjectFilters();
    initContactForm();
    initTypingEffect();
    
    // Log that the site is loaded
    console.log('🚀 Portfolio website loaded successfully!');
});

/**
 * Smooth scrolling for navigation links
 */
function initSmoothScrolling() {
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 80; // Account for fixed navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Initialize scroll-based animations
 */
function initAnimations() {
    // Create intersection observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.card, .skill-category, .stat-card');
    animatedElements.forEach(el => observer.observe(el));
}

/**
 * Navbar scroll effects
 */
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
    
    // Add custom styles for scrolled navbar
    const style = document.createElement('style');
    style.textContent = `
        .navbar-scrolled {
            background-color: rgba(52, 58, 64, 0.95) !important;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
    `;
    document.head.appendChild(style);
}

/**
 * Project filtering functionality (for projects page)
 */
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('[data-filter]');
    const projectItems = document.querySelectorAll('.project-item');
    
    if (filterButtons.length === 0) return; // Not on projects page
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Filter projects with animation
            projectItems.forEach(item => {
                const category = item.getAttribute('data-category');
                
                if (filter === 'all' || category === filter) {
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0)';
                    }, 100);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
            
            // Add ripple effect to button
            addRippleEffect(this);
        });
    });
}

/**
 * Contact form enhancements
 */
function initContactForm() {
    const contactForm = document.getElementById('contact-form');
    
    if (!contactForm) return; // Not on contact page
    
    // Add real-time validation
    const inputs = contactForm.querySelectorAll('input, textarea');
    
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            // Remove error state when user starts typing
            if (this.classList.contains('is-invalid')) {
                this.classList.remove('is-invalid');
            }
        });
    });
    
    // Enhanced form submission
    contactForm.addEventListener('submit', function(e) {
        let isValid = true;
        
        inputs.forEach(input => {
            if (!validateField(input)) {
                isValid = false;
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            showNotification('Please fix the errors in the form.', 'error');
            return;
        }
        
        // Add loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
        submitBtn.disabled = true;
        
        // Note: The form will be submitted normally after this
        // In a real implementation, you might handle this with AJAX
    });
}

/**
 * Validate individual form field
 */
function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let errorMessage = '';
    
    // Check if field is required and empty
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = 'This field is required.';
    }
    
    // Email validation
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address.';
        }
    }
    
    // Update field appearance
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
        
        // Show error message
        showFieldError(field, errorMessage);
    }
    
    return isValid;
}

/**
 * Show error message for field
 */
function showFieldError(field, message) {
    // Remove existing error message
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
    
    // Add new error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentNode.appendChild(errorDiv);
}

/**
 * Typing effect for hero section
 */
function initTypingEffect() {
    const titleElement = document.querySelector('.hero-section h2');
    
    if (!titleElement) return;
    
    const titles = [
        'Web Developer & Programming Enthusiast',
        'Frontend Developer',
        'Backend Developer',
        'Full Stack Developer',
        'Problem Solver'
    ];
    
    let currentTitleIndex = 0;
    let currentCharIndex = 0;
    let isDeleting = false;
    
    function typeEffect() {
        const currentTitle = titles[currentTitleIndex];
        
        if (isDeleting) {
            titleElement.textContent = currentTitle.substring(0, currentCharIndex - 1);
            currentCharIndex--;
        } else {
            titleElement.textContent = currentTitle.substring(0, currentCharIndex + 1);
            currentCharIndex++;
        }
        
        let typeSpeed = isDeleting ? 50 : 100;
        
        if (!isDeleting && currentCharIndex === currentTitle.length) {
            typeSpeed = 2000; // Pause at end
            isDeleting = true;
        } else if (isDeleting && currentCharIndex === 0) {
            isDeleting = false;
            currentTitleIndex = (currentTitleIndex + 1) % titles.length;
            typeSpeed = 500; // Pause before starting new title
        }
        
        setTimeout(typeEffect, typeSpeed);
    }
    
    // Start typing effect after a delay
    setTimeout(typeEffect, 1000);
}

/**
 * Add ripple effect to buttons
 */
function addRippleEffect(element) {
    const ripple = document.createElement('span');
    const rect = element.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;
    
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.className = 'ripple';
    
    // Add ripple styles
    const style = document.createElement('style');
    style.textContent = `
        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple-animation 0.6s linear;
            pointer-events: none;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    element.style.position = 'relative';
    element.style.overflow = 'hidden';
    element.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
}

/**
 * Show notification messages
 */
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    `;
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" onclick="this.parentElement.remove()"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 5000);
}

/**
 * Lazy loading for images
 */
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

/**
 * Initialize copy to clipboard functionality
 */
function initClipboard() {
    const copyButtons = document.querySelectorAll('[data-copy]');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const textToCopy = this.getAttribute('data-copy');
            
            navigator.clipboard.writeText(textToCopy).then(() => {
                showNotification('Copied to clipboard!', 'success');
            }).catch(() => {
                showNotification('Failed to copy to clipboard.', 'error');
            });
        });
    });
}

/**
 * Back to top button
 */
function initBackToTop() {
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopBtn.className = 'btn btn-primary position-fixed';
    backToTopBtn.style.cssText = `
        bottom: 30px;
        right: 30px;
        z-index: 999;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: none;
        box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
    `;
    
    document.body.appendChild(backToTopBtn);
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });
    
    // Scroll to top when clicked
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Initialize back to top button
initBackToTop();

/**
 * Parallax effect for hero section
 */
function initParallax() {
    const heroSection = document.querySelector('.hero-section');
    
    if (!heroSection) return;
    
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.5;
        
        heroSection.style.transform = `translateY(${rate}px)`;
    });
}

// Initialize parallax effect
// Commented out by default to avoid motion sickness for some users
// initParallax();

/**
 * Dark mode toggle (optional feature)
 */
function initDarkMode() {
    const darkModeToggle = document.createElement('button');
    darkModeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    darkModeToggle.className = 'btn btn-outline-light position-fixed';
    darkModeToggle.style.cssText = `
        top: 100px;
        right: 30px;
        z-index: 999;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: none; // Hidden by default, uncomment to enable
    `;
    
    document.body.appendChild(darkModeToggle);
    
    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        
        const icon = this.querySelector('i');
        if (document.body.classList.contains('dark-mode')) {
            icon.className = 'fas fa-sun';
            localStorage.setItem('darkMode', 'enabled');
        } else {
            icon.className = 'fas fa-moon';
            localStorage.setItem('darkMode', 'disabled');
        }
    });
    
    // Check for saved dark mode preference
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
        darkModeToggle.querySelector('i').className = 'fas fa-sun';
    }
}

// Performance monitoring
const perfObserver = new PerformanceObserver((list) => {
    list.getEntries().forEach((entry) => {
        if (entry.entryType === 'navigation') {
            console.log(`🚀 Page load time: ${entry.loadEventEnd - entry.loadEventStart}ms`);
        }
    });
});
