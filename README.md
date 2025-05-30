# django datatable builder

Reusable component to generate dynamic datatables in Django projects, with Bootstrap support and customizable row actions.

[![PyPI version](https://badge.fury.io/py/django-datatable-builder.svg)](https://pypi.org/project/django-datatable-builder/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🚀 Features

- Automatically generate HTML tables from Django QuerySets
- Supports pagination, ordering, and search
- Bootstrap-compatible out of the box
- Custom row-level actions (edit, delete, etc.)
- Easy integration into existing Django apps

---

## 📦 Installation

```bash
pip install django-datatable-builder
```

## 🛠️ Basic Usage

#### 1.Add to INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...
    'django_datatable_builder',
]
```


#### 2.Create a table class in your view:

```python
from django_datatable_builder import DataTable

def datatable_view(request):
    devices = [
        {"id": 1, "name": "Router", "status": "Active"},
        {"id": 2, "name": "Switch", "status": "Inactive"},
    ]

    datatable_config = {
        "data": devices,
        "columns": ["Name", "Status"],
        "hidden": ["id"],
        "order": [[0, "asc"]],
        "table_id": "devices_table",
        "column_search": True,
        "button_dropdown": True,
        "button_url": {
            "Show_demo_1": {"link": {"url": "demo:datatable_view",}},
            "Show_demo_2": {"modal": {"url": "demo:datatable_view","params":"devices_id": "id"}}
        },
        "button_inline": {
            "Show_demo_3": {"link": {"url": "demo:datatable_view", "params": {"devices_id": "id"}}, "class": "btn btn-success float-end"},
        },
    }

    return render(request, "demo.html", {"datatable": DataTable(request, datatable_config)})
```


#### 3.Render the table in your template:

```python
{{ datatable|safe }}
```

## 📚 Documentation

### **`DataTable` Parameters**

These are the main configuration options used to initialize and render a dynamic datatable.

| Parameter         | Description                                                                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`data`**            | A Django `QuerySet` or a `list` of dictionaries. This is the source of the table content.                                                                          |
| **`columns`**         | A list of column names. **Order must match** the order of fields in `data`.                                                                                        |
| **`hidden`**          | A list of field names to **hide from the table**. Useful for keeping some values available in HTML without displaying them.                                        |
| **`order`**           | Default ordering of the table. Format: `[[column_index, "asc" or "desc"]]` — e.g., `[[0, "asc"]]`.                                                                 |
| **`table_id`**        | The HTML `id` attribute of the table. Required for JavaScript initialization.                                                                                      |
| **`column_search`**   | A list of field names that should support **column-specific search**.                                                                                              |
| **`button_dropdown`** | Set to `true` or `false` depending on whether you want to show a dropdown with action buttons per row.                                                             |
| **`button_urls`**     | Used with `button_dropdown`. Defines one or more buttons with types like `"link"` or `"modal"`. Supports optional `class`, and `params`. See example below. |
| **`button_inline`**   | Used for inline buttons (outside dropdowns). Structure is similar to `button_urls`. Useful if you want more flexibility with custom buttons.                       |


`button_urls` **(used with dropdown buttons)**

```python
button_urls = {
    "Edit": {
        "modal": {
            "url": "/edit/",
            "params": {
                "id": "id"  # Uses the 'id' from each row in `data`
            }
            "class": "btn btn-sm btn-primary",
        }
    },
    "View": {
        "link": {
            "url": "/view/",
        }
        "class": "btn btn-sm btn-secondary"
    }
}
```

`button_inline` **(buttons directly rendered in table row)**

```python
button_inline = {
    "Delete": {
        "modal": {
            "url": "/delete/",
            "params": {
                "id": "id"
            }
        }
    }
}

```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.