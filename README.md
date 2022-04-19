# Django-template-name mocking

Proof of concept for mocking Django template rendering
in a way where template names are added at the top
of the rendered content.

## What?

Given these two templates
```html
# base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Base</title>
</head>
<body>
Base template
{% include 'nested.html' %}
</body>
</html>
```

```html
# nested.html
Nested template
```

We want the rendered content to look like this

```html
<!-- template name: base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Base</title>
</head>
<body>
Base template
<!-- template name: base.html -->
Nested template
</body>
</html>
```

## Why?

To provide a simple way of drilling down to specific content,
with a rendered view as the starting point. 

Without tags like this it can be very hard to identify deeply 
nested templates in larger projects.

That being said, there might be better ways of doing this/well 
established tools that do similar things that I don't know about.
