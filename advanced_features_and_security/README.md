# ================================
# 📘 Permissions & Groups Overview
# ================================
# Custom permissions defined in models.py:
#   can_view   → Allows viewing of Book instances
#   can_create → Allows creation of Book instances
#   can_edit   → Allows editing of Book instances
#   can_delete → Allows deletion of Book instances
#
# Groups created via management command:
#   Viewers → can_view
#   Editors → can_view, can_create, can_edit
#   Admins  → can_view, can_create, can_edit, can_delete
#
# Usage in Views:
#   @permission_required('bookshelf.can_view')   → Protects viewing
#   @permission_required('bookshelf.can_edit')   → Protects editing
#   @permission_required('bookshelf.can_create') → Protects adding
#
# Purpose:
#   These permissions and groups ensure role-based access control (RBAC)
#   within the Django application for better security and organization.
# ================================
