from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TokenClassificationAggregationsMentionsAdditionalProperty")


@attr.s(auto_attribs=True)
class TokenClassificationAggregationsMentionsAdditionalProperty:
    """  """

    additional_properties: Dict[str, int] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token_classification_aggregations_mentions_additional_property = cls()

        token_classification_aggregations_mentions_additional_property.additional_properties = (
            d
        )
        return token_classification_aggregations_mentions_additional_property

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
