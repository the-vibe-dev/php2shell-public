"""Small invariant models. No PHP, network, payloads, processes, or file writes.

These models are illustrations, NOT reproductions of the underlying CVEs.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json


@dataclass(frozen=True)
class Observation:
    model: str
    result: str
    boundary: str
    is_php_reproduction: bool = False


def partial_state(interrupted: bool, discard_incomplete: bool) -> Observation:
    """Represent initialization by a boolean, never by corrupt memory."""
    if interrupted and not discard_incomplete:
        result = "cleanup_assumption_violated"
    elif interrupted:
        result = "incomplete_state_not_consumed"
    else:
        result = "initialized_state"
    return Observation("partial-state", result, "abstract initialization state only")


def request_lifetime(owner_generation: int, current_generation: int, reset: bool) -> Observation:
    """Compare abstract request generations; no pointers or memory access."""
    for value in (owner_generation, current_generation):
        if type(value) is not int or value < 0:
            raise ValueError("generations must be nonnegative integers")
    result = "reference_cleared" if reset else (
        "stale_reference_model" if owner_generation != current_generation else "same_lifetime"
    )
    return Observation("request-lifetime", result, "generation labels are not worker scheduling")


def format_agreement(writer: str, reader: str, reject_mismatch: bool = True) -> Observation:
    """Use invented format labels, not PHP syntax or executable object data."""
    if writer not in ("format-A", "format-B") or reader not in ("format-A", "format-B"):
        raise ValueError("only the two abstract format labels are accepted")
    if writer == reader:
        result = "format_consistent"
    else:
        result = "mismatch_rejected" if reject_mismatch else "interpretation_boundary_changed"
    return Observation("format-agreement", result, "no serializer or deserializer is implemented")


def reader_boundary(record_present: bool, independent_sink_present: bool) -> Observation:
    """Model prerequisites without opening or including a file."""
    if not record_present:
        result = "no_record"
    elif not independent_sink_present:
        result = "stored_data_without_reader"
    else:
        result = "independent_application_boundary_needed"
    return Observation("reader-boundary", result, "no application or inclusion path is implemented")


def application_requirements(object_source: bool, reader: bool, side_effect: bool) -> Observation:
    """A conjunction is not proof of an actual application's reachability."""
    result = "assumptions_present_not_execution_proof" if all((object_source, reader, side_effect)) else "incomplete_claim"
    return Observation("application-requirements", result, "booleans do not establish a stock-application chain")


def demonstration() -> list[Observation]:
    return [
        partial_state(True, False), partial_state(True, True),
        request_lifetime(1, 2, False), request_lifetime(1, 2, True),
        format_agreement("format-A", "format-B", False),
        format_agreement("format-A", "format-B", True),
        reader_boundary(True, False), reader_boundary(True, True),
        application_requirements(False, True, True),
        application_requirements(True, True, True),
    ]


if __name__ == "__main__":
    print("EDUCATIONAL MODEL — NOT PHP REPRODUCTION")
    print(json.dumps([asdict(item) for item in demonstration()], indent=2))
