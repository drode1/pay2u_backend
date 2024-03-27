from django.utils import timezone


def soft_delete_object(obj) -> None:
    if obj.deleted_at:
        return None

    obj.deleted_at = timezone.now()
    obj.save(update_fields=['deleted_at'])

    return None


def recover_object(obj) -> None:
    obj.deleted_at = None
    obj.save(update_fields=['deleted_at'])

    return None
