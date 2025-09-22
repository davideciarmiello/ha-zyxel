from __future__ import annotations

from typing import Any
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import *

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    #coordinator = entry.runtime_data    
    router = hass.data[DOMAIN][entry.entry_id]["router"]
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]

    return {        
        "coordinator_data": coordinator.data
    }