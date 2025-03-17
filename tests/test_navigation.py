import pytest
from playwright.sync_api import Page, expect

def login(page: Page):
    """Helper function to log in the user"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    expect(page).to_have_title("Rahul's Blogs")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")

def test_home_navigation(page: Page):
    """Test navigation to home page"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.click("a[href='/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")

def test_post_detail_navigation(page: Page):
    """Test navigation to post detail page"""
    page.goto("http://127.0.0.1:8000/")
    page.click("a[href='/post/14/']")
    expect(page).to_have_url("http://127.0.0.1:8000/post/14/")
    expect(page.locator("h2")).to_have_text("Updated Test Post")  # Replace "Post Title" with the actual title

def test_edit_post_navigation(page: Page):
    """Test navigation to edit post page"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.click("a[href='/post/14/']")
    page.click("a[href='/post/14/edit/']")
    expect(page.locator("button[type='submit']")).to_have_text("Publish")
    expect(page.locator("button#add-snippet")).to_have_text("Add Code Snippet")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")


def test_unauthorized_access(page: Page):
    """Test unauthorized access to protected pages"""
    page.goto("http://127.0.0.1:8000/post/new/")
    expect(page).to_have_url("http://127.0.0.1:8000/login/?next=/post/new/")
    page.goto("http://127.0.0.1:8000/post/14/edit/")
    expect(page).to_have_url("http://127.0.0.1:8000/login/?next=/post/14/edit/")