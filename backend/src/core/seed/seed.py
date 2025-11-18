"""Seed script for development/CI.

Usage from the `backend/` folder:
  python -m src.core.seed.seed

This script loads `seed_data.json` (same folder) and inserts cafes and items.
It is idempotent: it will not duplicate cafes with the same (name, location)
and will not duplicate items with the same (name, cafe_id).
"""
from pathlib import Path
import json
from typing import Any

from src.core.db import SessionLocal, create_db_and_tables
from src.core.models.cafe import Cafe
from src.core.models.item import Item


SEED_JSON = Path(__file__).with_name("seed_data").joinpath("seed_data.json")


def seed_from_json(session) -> None:
	if not SEED_JSON.exists():
		print(f"No seed file found at {SEED_JSON}")
		return

	with SEED_JSON.open("r", encoding="utf-8") as f:
		data = json.load(f)

	cafes = data.get("cafes", [])

	for cafe_data in cafes:
		name = cafe_data.get("name")
		location = cafe_data.get("location")

		existing = (
			session.query(Cafe)
			.filter(Cafe.name == name, Cafe.location == location)
			.first()
		)

		if existing:
			cafe = existing
		else:
			cafe = Cafe(
				name=name,
				location=location,
				cafe_rating=cafe_data.get("cafe_rating"),
				menu_rating=cafe_data.get("menu_rating"),
				image_url=cafe_data.get("image_url"),
			)
			session.add(cafe)
			session.flush()

		for item_data in cafe_data.get("items", []):
			item_name = item_data.get("name")
			exists_item = (
				session.query(Item)
				.filter(Item.name == item_name, Item.cafe_id == cafe.id)
				.first()
			)
			if exists_item:
				continue

			item = Item(
				name=item_data.get("name"),
				description=item_data.get("description"),
				rating=item_data.get("rating"),
				notes=item_data.get("notes"),
				image_url=item_data.get("image_url"),
				cafe_id=cafe.id,
			)
			session.add(item)

	session.commit()


def main() -> None:
	create_db_and_tables()
	db = SessionLocal()
	try:
		seed_from_json(db)
		print("Seeding complete")
	finally:
		db.close()


if __name__ == "__main__":
	main()


