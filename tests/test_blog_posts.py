import pytest
from playwright.sync_api import Page, expect
import re

def test_post_list_page_loads(page: Page):
    """Test that post list page loads correctly"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    expect(page).to_have_title("Rahul's Blogs")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")

def test_create_new_post(page: Page):
    """Test creating a new blog post"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.goto("http://127.0.0.1:8000/post/new/")
    page.fill("input[name='title']", "Test Post")
    page.fill("textarea[name='text']", "This is a test post.")
    page.click("button[type='submit']")
   # Use regex to match the URL
    assert re.match(r"http://127.0.0.1:8000/post/\d+/", page.url)
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")

def test_edit_existing_post(page: Page):
    """Test editing an existing post"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.click("a[href='/post/14/']")
    page.click("a[href='/post/14/edit/']")
    page.fill("input[name='title']", "Updated Test Post")
    page.fill("textarea[name='text']", "This is an updated test post.")
    page.click("button[type='submit']")
    expect(page).to_have_url("http://127.0.0.1:8000/post/14/")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")

# '''def test_delete_post(page: Page):
#     """Test deleting a post"""
#     login(page)
#     page.goto("http://127.0.0.1:8000/")
#     page.click("a[href='/post/1/delete/']")
#     page.click("button[type='submit']")
#     expect(page).to_have_url("http://127.0.0.1:8000/")
# '''

def test_search_posts(page: Page):
    """Test post search functionality"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.fill("input[placeholder='type something...']", "search")
    page.click("button[type='submit']")
    expect(page.locator(".card")).to_have_count(1)
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")