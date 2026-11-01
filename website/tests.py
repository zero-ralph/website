import io
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from PIL import Image
from .models import LandingPage, Project


# Create your tests here.
class LandingPageTestCase(TestCase):
    def setUp(self):
        file_object = io.BytesIO()
        image = Image.new("RGBA", size=(1, 1), color=(256,0,0))
        image.save(file_object, "png")
        file_object.seek(0)
        

        self.uploaded_image = SimpleUploadedFile(
            name="test_image.png",
            content=file_object.read(),
            content_type="image/png"
        )


        LandingPage.objects.create(
            logo=self.uploaded_image,
            name="ralph",
            overview="ralph overview",
            about_me="ralph about me",
            email="ralph.subrio@gmail.com",
            github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
            linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
        )

    def test_landing_page_with_complete_and_valid_data(self):
        page = LandingPage.objects.get(id=1)
        self.assertEqual(page.name, "ralph")
        self.assertEqual(page.overview, "ralph overview")
        self.assertEqual(page.about_me, "ralph about me")
        self.assertEqual(page.email, "ralph.subrio@gmail.com")
        self.assertEqual(page.github_link, "https://github.com/zero-ralph/website/actions/runs/40479248598")
        self.assertEqual(page.linkedin_link, "https://www.linkedin.com/in/ralphsubrio/")
        
    def test_landing_page_with_missing_logo(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                name="ralph",
                overview="ralph overview",
                about_me="ralph about me",
                email="ralph.subrio@gmail.com",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()

    def test_landing_page_with_missing_name(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                overview="ralph overview",
                about_me="ralph about me",
                email="ralph.subrio@gmail.com",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()

    def test_landing_page_with_missing_overview(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                about_me="ralph about me",
                email="ralph.subrio@gmail.com",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()

    def test_landing_page_with_missing_about_me(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                overview="ralph overview",
                email="ralph.subrio@gmail.com",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()

    def test_landing_page_with_missing_email(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                overview="ralph overview",
                about_me="ralph about me",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()

    def test_landing_page_with_missing_github_link(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                overview="ralph overview",
                email="ralph.subrio@gmail.com",
                about_me="ralph about me",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()

    def test_landing_page_with_missing_linkedin_link(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                overview="ralph overview",
                email="ralph.subrio@gmail.com",
                about_me="ralph about me",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
            ).full_clean()


    def test_landing_page_with_email_must_be_correct_email_structure(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                overview="ralph overview",
                about_me="ralph about me",
                email="ralph.subrio",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()
    
    def test_landing_page_with_github_link_must_be_correct_url_structur(self):
       with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                overview="ralph overview",
                about_me="ralph about me",
                email="ralph.subrio@gmail.com",
                github_link="github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="https://www.linkedin.com/in/ralphsubrio/"
            ).full_clean()
    def test_landing_page_with_linkedin_link_must_be_correct_url_structure(self):
        with self.assertRaises(ValidationError):
            LandingPage.objects.create(
                logo=self.uploaded_image,
                name="ralph",
                overview="ralph overview",
                about_me="ralph about me",
                email="ralph.subrio@gmail.com",
                github_link="https://github.com/zero-ralph/website/actions/runs/40479248598",
                linkedin_link="linkedin.com/in/ralphsubrio/"
            ).full_clean()


class ProjectTestCase(TestCase):

    def setUp(self):
        self.date = timezone.now()
        Project.objects.create(
            title="project 1",
            short_description="This is project 1",
            created_at=self.date
        )

    def test_project_with_complete_data(self):
        project = Project.objects.get(id=1)
        self.assertEqual(project.title, "project 1")
        self.assertEqual(project.short_description, "This is project 1")
        self.assertEqual(project.created_at, self.date)

    def test_project_missing_title(self):
        with self.assertRaises(ValidationError):
            Project.objects.create(
                short_description="This is project 1",
                created_at=self.date
            ).full_clean()

    def test_project_missing_short_description(self):
        with self.assertRaises(ValidationError):
            Project.objects.create(
                title="project 1",
                created_at=self.date
            ).full_clean()

    def test_project_missing_created_at(self):
        with self.assertRaises(ValidationError):
            Project.objects.create(
                title="project 1",
                short_description="This is project 1",
            ).full_clean()