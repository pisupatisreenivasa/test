from typing import List, Optional


class InvalidClaimDataException(Exception):
    pass

class Claim:
    def __init__(self, data: str):
        self.data = data

    def __str__(self):
        return f"Claim(data={self.data})"

class ClaimsProcessor:
    def __init__(self):
        self.claims_cache: List[Claim] = []

    def process_new_claim(self, claim_data: str):
        try:
            claim = self.parse_claim_data(claim_data)
            if claim:
                self.claims_cache.append(claim)
                print(f"Claim processed successfully: {claim}")
            else:
                print("No data to process.")
        except InvalidClaimDataException as e:
            print(f"Invalid claim data: {str(e)}")

    def parse_claim_data(self, data: str) -> Optional[Claim]:
        cleaned_data = data.strip()
        if cleaned_data:
            return Claim(cleaned_data)
        raise InvalidClaimDataException("Claim data is empty or contains only whitespace.")

    def get_claims(self) -> List[Claim]:
        return self.claims_cache.copy()