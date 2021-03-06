# Django PSI

[![Build Status](https://travis-ci.org/vintasoftware/django-psi.svg?branch=develop)](https://travis-ci.org/vintasoftware/django-psi)
[![codecov](https://codecov.io/gh/vintasoftware/django-psi/branch/develop/graph/badge.svg)](https://codecov.io/gh/vintasoftware/django-psi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Django PSI is a tool for generating and visualizing Page Speed performance reports using Google's PSI API.
Have a timeline with your score progress, integrate to your CI tool and enable performance tracking per release.

## Requirements:
- A PostgreSQL Database in your Django project (for JSON fields)
- Google API Dev Credentials

### Optional:
- A Slack webhook to send notifications to.

## Quickstart

1. Add the following settings to your Django project
```python
PSI_GOOGLE_API_DEV_KEY = 'MYKEY'
PSI_SLACK_MESSAGE_HOOK = 'http://myslackmessagehook/zxcvbn'
PSI_FULL_ADMIN_PATH = 'https://example-site.com/admin'
PSI_ENVS = {
    'production': {
        'base_url': 'https://example-site.com',
    },
    'staging': {
        'base_url': 'https://staging-example-site.com',
    }
}
```

2. Add Django PSI to installed apps

```python
INSTALLED_APPS = [
    ...
    'djangopsi',
    ...
]
```

3. Decorate your class-based views with `@is_psi_checked`

```python
from djangopsi.decorators import is_psi_checked


@is_psi_checked
class ExampleView(generic.TemplateView):
    ...
```

4. Run command run_psi_check, or add it to your CI process.

`python manage.py run_psi_check -c -k --slack-message`

Options:

```
-c --console
    Outputs the report in the console

--env=ENV
    Env in which the analysis will be made. Default value is `production`.

-k --keep
    Persist the report to the database

--strategy=STRATEGY
    Strategy to be used on the analysis. Default value is `all` (desktop and mobile).

--slack-message
    Notifies and links on Slack about the report made.
```

## Security

Please check SECURITY.md. If you found or if you think you found a vulnerability please get in touch via admin AT vinta.com.br

Please avoid disclosing any security issue on GitHub or any other public website. We'll work to swiftly address any possible vulnerability and give credit to reporters (if wanted).

## Commercial Support

This project is maintained by Vinta Software and other contributors. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br