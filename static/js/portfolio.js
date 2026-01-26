/**
 * Interactive Portfolio JavaScript
 * Handles filtering, animations, smooth scrolling, and UI interactions
 */

// ==================== INITIALIZATION ====================
document.addEventListener('DOMContentLoaded', function () {
    initMobileMenu();
    initProjectFilters();
    initSmoothScrolling();
    initScrollAnimations();
    initActiveNavLinks();
});

// ==================== MOBILE MENU ====================
function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', function () {
            navLinks.classList.toggle('active');
        });

        // Close menu when clicking a link
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', function () {
                navLinks.classList.remove('active');
            });
        });
    }
}

// ==================== PROJECT FILTERING ====================
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    if (filterButtons.length === 0) return;

    filterButtons.forEach(button => {
        button.addEventListener('click', function () {
            const category = this.getAttribute('data-category');

            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filter projects with animation
            projectCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');

                if (category === 'All' || cardCategory === category ||
                    (card.getAttribute('data-tags') && card.getAttribute('data-tags').includes(category))) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 10);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
}

// ==================== SMOOTH SCROLLING ====================
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');

            // Skip if it's just "#" or if target doesn't exist
            if (href === '#' || !document.querySelector(href)) return;

            e.preventDefault();
            const target = document.querySelector(href);

            if (target) {
                const offset = 80; // Account for fixed navbar
                const targetPosition = target.offsetTop - offset;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ==================== SCROLL ANIMATIONS ====================
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.fade-in-up, .card, .timeline-item');

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animatedElements.forEach(element => {
        // Set initial state
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';

        observer.observe(element);
    });
}

// ==================== ACTIVE NAV LINKS ====================
function initActiveNavLinks() {
    const navLinks = document.querySelectorAll('.nav-links a');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;

        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });
}

// ==================== CONTACT FORM (Optional Enhancement) ====================
function initContactForm() {
    const form = document.querySelector('.contact-form');

    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(form);
            const data = Object.fromEntries(formData);

            console.log('Contact form submitted:', data);

            // Show success message
            alert('Thank you for your message! I will get back to you soon.');
            form.reset();
        });
    }
}

// ==================== CV DEMO CHATBOT (If on chatbot page) ====================
if (document.getElementById('chatbot-form')) {
    const chatForm = document.getElementById('chatbot-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', async function (e) {
        e.preventDefault();

        const query = chatInput.value.trim();
        if (!query) return;

        // Add user message to chat
        addMessage('user', query);
        chatInput.value = '';

        // Show loading
        const loadingId = addMessage('assistant', 'Thinking...');

        try {
            const response = await fetch('/api/cv-demo/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query: query })
            });

            const data = await response.json();

            // Remove loading message
            document.getElementById(loadingId).remove();

            if (data.error) {
                addMessage('assistant', 'Error: ' + data.error);
            } else {
                addMessage('assistant', data.response);
            }
        } catch (error) {
            document.getElementById(loadingId).remove();
            addMessage('assistant', 'Error: Failed to get response');
        }

        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    });

    function addMessage(role, content) {
        const messageId = 'msg-' + Date.now();
        const messageDiv = document.createElement('div');
        messageDiv.id = messageId;
        messageDiv.className = `chat-message ${role}-message`;
        messageDiv.innerHTML = `
            <div class="message-content">
                ${content}
            </div>
        `;
        chatMessages.appendChild(messageDiv);
        return messageId;
    }
}

// ==================== UTILITY FUNCTIONS ====================
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add loading state to buttons
function setButtonLoading(button, loading) {
    if (loading) {
        button.dataset.originalText = button.textContent;
        button.textContent = 'Loading...';
        button.disabled = true;
    } else {
        button.textContent = button.dataset.originalText || button.textContent;
        button.disabled = false;
    }
}
