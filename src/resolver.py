def resolve_steam_id(raw_input: str) -> dict:

    cleaned = string_cleanup(raw_input)

    cleaned = cleaned.replace("https://","")

    if "/id/" in cleaned:
        vanity_name = cleaned.split("/id/")[1]
        return output_convention(False, None, "WIP", "Not Yet Implemented")
        # TODO ResolveVanityURL

    elif "/profiles/" in cleaned:
        raw_id = cleaned.split("/profiles/")[1]
        return output_convention(True, raw_id, None, None)
    
    elif cleaned.startswith("7656") and len(cleaned) == 17 and cleaned.isnumeric():
        raw_id = cleaned
        return output_convention(True, raw_id, None, None)
    else:
        return output_convention(False, None, "UNCLASSIFIED_ERROR", "This error has not been classified")
    


def string_cleanup(input_string: str) -> str:

    input_string = input_string.strip()
    input_string = input_string.lower()

    if "https://" not in input_string and "http://" not in input_string:
        input_string = "https://" + input_string

    if "?" in input_string:
        input_string = input_string.split("?")[0]

    if input_string.endswith("/"):
        input_string = input_string[:-1]

    return input_string
