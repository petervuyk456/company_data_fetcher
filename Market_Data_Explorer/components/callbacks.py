def toggle_navbar_collapse():
    def navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    return navbar_collapse
