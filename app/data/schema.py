"""Schema definitions for customer analytics datasets."""
from dataclasses import dataclass, field

@dataclass(frozen=True)
class CustomerCSVSchema:
    required_columns: set[str] = field(
        default_factory=lambda: {
            "CUSTOMER ID",
            "DEPARTMENT STORE",
            "TOTAL SPEND",
            "PURCHASES",
            "AVG ORDER VALUE",
            "TENURE DAYS",
            "LAST PURCHASE DAYS",
            "RETURNS",
            "CANCELLATIONS",
        }
    )
    optional_columns: set[str] = field(
        default_factory=lambda: {
            "EMAIL",
            "REGION",
            "CHANNEL",
            "CUSTOMER SEGMENT",
            "REVENUE",
        }
    )

CUSTOMER_SCHEMA = CustomerCSVSchema()