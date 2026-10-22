from yoyo import step

steps = [
    step(
        """
        ALTER TABLE posts
        ADD COLUMN created_at TEXT
        """,
        None,
    )
]
