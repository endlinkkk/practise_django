
def is_administrators_group(user) -> bool:
    return user.groups.filter(name='administrators').exists()


def is_master_group(user) -> bool:
    return user.groups.filter(name='master').exists()


def is_administrator_or_master(user) -> bool:
    return user.groups.filter(name__in=['administrators', 'master']).exists()