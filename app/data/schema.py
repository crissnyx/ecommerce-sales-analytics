"""Schema definitions for customer analytics datasets."""
<<<<<<< HEAD
from dataclasses import dataclass, field

=======

from dataclasses import dataclass, field


>>>>>>> origin/feat/project-structure
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

<<<<<<< HEAD
CUSTOMER_SCHEMA = CustomerCSVSchema()
=======

CUSTOMER_SCHEMA = CustomerCSVSchema()
>>>>>>> origin/feat/project-structure
