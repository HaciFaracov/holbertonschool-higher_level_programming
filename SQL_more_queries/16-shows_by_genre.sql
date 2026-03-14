-- lists all shows and all genres linked to that show
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
```

---

### 📖 Explanation

This combines everything we've learned about JOINs!

**Two `LEFT JOIN`s** — we use `LEFT JOIN` for both because we need ALL shows to appear even if they have no genre linked (like `Better Call Saul` and `Homeland` which show `NULL`).

The chain:
```
tv_shows → tv_show_genres → tv_genres
