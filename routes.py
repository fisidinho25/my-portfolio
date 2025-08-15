from flask import render_template, request, flash, redirect, url_for
from app import app, db
from models import ContactSubmission
from data.projects import PROJECTS, PERSONAL_INFO, SKILLS
import logging
@app.route('/')
def index():
    featured_projects = PROJECTS[:6]
    return render_template('index.html', featured_projects=featured_projects, personal_info=PERSONAL_INFO, skills=SKILLS)
@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS, personal_info=PERSONAL_INFO)
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    
    if not project:
        flash('Project not found.', 'error')
        return redirect(url_for('projects'))
    
    return render_template('project_detail.html', project=project, personal_info=PERSONAL_INFO, projects=PROJECTS)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        if not all([name, email, subject, message]):
            flash('All fields are required.', 'error')
            return render_template('contact.html', personal_info=PERSONAL_INFO)
        
        try:
            submission = ContactSubmission(name=name, email=email, subject=subject, message=message)
            db.session.add(submission)
            db.session.commit()
            flash('Thank you for your message! I will get back to you soon.', 'success')
            logging.info(f"Contact form submitted by {name} ({email})")
            return redirect(url_for('contact'))
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error saving contact form: {e}")
            flash('Sorry, there was an error sending your message. Please try again.', 'error')
    
    return render_template('contact.html', personal_info=PERSONAL_INFO)
@app.errorhandler(404)
def not_found_error(error):
    return render_template('base.html', personal_info=PERSONAL_INFO), 404
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('base.html', personal_info=PERSONAL_INFO), 500