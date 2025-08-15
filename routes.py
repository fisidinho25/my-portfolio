from flask import render_template, request, flash, redirect, url_for
from app import app, db
from models import ContactSubmission
from models import Todo
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

@app.route('/todos')
def todos():
    """Todo list page"""
    todos = Todo.query.all()
    return render_template('todos.html', todos=todos, personal_info=PERSONAL_INFO)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    """Add a new todo"""
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    
    if title:
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
        flash('Todo added successfully!', 'success')
    else:
        flash('Title is required!', 'error')
    
    return redirect(url_for('todos'))

@app.route('/complete_todo/<int:todo_id>')
def complete_todo(todo_id):
    """Toggle todo completion status"""
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    flash(f'Todo {"completed" if todo.completed else "marked as active"}!', 'success')
    return redirect(url_for('todos'))

@app.route('/delete_todo/<int:todo_id>')
def delete_todo(todo_id):
    """Delete a todo"""
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted!', 'info')
    return redirect(url_for('todos'))

@app.errorhandler(404)
def not_found_error(error):
    """Custom 404 error page"""
    return render_template('base.html', personal_info=PERSONAL_INFO), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error page"""
    db.session.rollback()
    return render_template('base.html', personal_info=PERSONAL_INFO), 500
