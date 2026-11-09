"""Convert the website's CV fields to RenderCV's PDF input schema."""

import argparse
import copy
from pathlib import Path

import yaml


def prepare_rendercv(data):
    document = copy.deepcopy(data)
    cv = document["cv"]
    if "label" in cv:
        cv["headline"] = cv.pop("label")
    if "image" in cv:
        image = cv.pop("image")
        if image:
            cv["photo"] = image

    sections = cv.setdefault("sections", {})
    summary = cv.pop("summary", None)
    if summary:
        sections = {"Profile": [summary, *sections.pop("Profile", [])], **sections}
        cv["sections"] = sections

    for entry in sections.get("Education", []):
        if "studyType" in entry:
            entry["degree"] = entry.pop("studyType")
        score = entry.pop("score", None)
        if score:
            entry.setdefault("highlights", []).append(str(score))

    for entry in sections.get("Publications", []):
        if "publisher" in entry:
            entry["journal"] = entry.pop("publisher")
        if "releaseDate" in entry:
            entry["date"] = entry.pop("releaseDate")

    skills = sections.get("Skills")
    if skills:
        sections["Skills"] = []
        for entry in skills:
            label = entry["name"]
            if entry.get("level"):
                label += f" ({entry['level']})"
            keywords = entry.get("keywords", "")
            details = ", ".join(keywords) if isinstance(keywords, list) else keywords
            sections["Skills"].append({"label": label, "details": details})

    for entry in sections.get("Awards", []):
        if "title" in entry:
            entry["name"] = entry.pop("title")
        awarder = entry.pop("awarder", None)
        if awarder:
            entry["summary"] = " - ".join(
                part for part in [entry.get("summary"), awarder] if part
            )

    return document


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    document = yaml.safe_load(args.source.read_text(encoding="utf-8"))
    args.destination.write_text(
        yaml.safe_dump(prepare_rendercv(document), sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
