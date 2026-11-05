def proverb(*args, qualifier=None):
    if not args:
        return []

    verses = [
        f"For want of a {first} the {second} was lost."
        for first, second in zip(args, args[1:])
    ]

    last = f"{qualifier} {args[0]}" if qualifier else args[0]
    verses.append(f"And all for the want of a {last}.")
    
    return verses
