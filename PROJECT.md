# Project: UniSafe Financial Survival Engine

## Architecture
- Backend: FastAPI app with SQLite database.
- Frontend: HTML/CSS/JS frontend (index.html).

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Explore & Plan | Investigate current backend/frontend implementation | None | DONE |
| 2 | Implementation | Implement pricing checkout, backend limits, scraper integration, double-click actions | M1 | DONE |
| 3 | Verification | Run integration tests (test_all.py) and check UI logic | M2 | DONE |

## Code Layout
- `tmp-integration-test/backend/main.py`: FastAPI endpoints
- `tmp-integration-test/backend/init_db.py`: Database schema and seeding
- `tmp-integration-test/frontend/index.html`: Main UI
