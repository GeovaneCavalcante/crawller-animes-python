def clear_pagination_text(pagination: str) -> 'list[int]':
    regex = "Paginade"
    for i in range(0, len(regex)):
        pagination = pagination.replace(regex[i], "")

    pagination = pagination.split(' ')

    return [int(x) for x in pagination if x > '']
