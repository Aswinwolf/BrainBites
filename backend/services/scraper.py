import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class WikiScraper:
    def __init__(self, url: str):
        self.url = url

    def validate_url(self):
        parsed = urlparse(self.url)

        if not parsed.scheme.startswith("http"):
            raise ValueError("Invalid URL scheme")

        if "wikipedia.org" not in parsed.netloc:
            raise ValueError("Only Wikipedia URLs are allowed")

    def fetch_page(self):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9"
        }

        response = requests.get(self.url, headers=headers, timeout=15)

        if response.status_code != 200:
            raise Exception("Failed to fetch the page")

        return response.text

    def parse(self):
        self.validate_url()
        html = self.fetch_page()

        # 🔍 DEBUG (you can remove later)
        # print("HTML LENGTH:", len(html))

        soup = BeautifulSoup(html, "html.parser")

        # ---------------- TITLE ----------------
        title = "No title found"
        title_tag = soup.find("h1", id="firstHeading")
        if title_tag:
            title = title_tag.get_text(strip=True)

        # ---------------- SUMMARY ----------------
        summary = ""

        # Try normal Wikipedia structure
        content_div = soup.find("div", class_="mw-parser-output")

        if content_div:
            for p in content_div.find_all("p"):
                text = p.get_text(strip=True)
                if text:
                    summary = text
                    break

        # Fallback: first real paragraph anywhere
        if not summary:
            for p in soup.find_all("p"):
                text = p.get_text(strip=True)
                if len(text) > 60:
                    summary = text
                    break

        # ---------------- SECTIONS ----------------
        sections = []

        # Standard Wikipedia headings
        for span in soup.select("h2 span.mw-headline, h3 span.mw-headline"):
            sections.append(span.get_text(strip=True))

        # Fallback if nothing found
        if not sections:
            for h in soup.find_all(["h2", "h3"]):
                text = h.get_text(strip=True)
                if text and not text.lower().startswith("references"):
                    sections.append(text)

        return {
            "title": title,
            "summary": summary,
            "sections": sections
        }
