import re

def normalize_price(price_str):
    if price_str is None:
        return price_str

    if isinstance(price_str, str):
        if 'reais' in price_str or 'centavos' in price_str:
            # Extract numeric parts of MercadoLivre format.
            parts = re.findall(r'\d+', price_str)
            if len(parts) == 2: # Received both reais and centavos.
                price_str = f"{parts[0]}.{parts[1]}"
            elif len(parts) == 1: # Received just the reais part.
                price_str = f"{parts[0]}.00"
        else:
            # Removes all non numeric characters, removing non ASCII characters from Magazine Luiza.
            price_str = re.sub(r'[^\d,\.]', '', price_str)
            # Removes thousands decimal brazilian representation.
            price_str = price_str.replace('.', '')
            # Replace the comma by a decimal point. 
            price_str = price_str.replace(',', '.')
        try:
            normalized_price = float(price_str)
            return normalized_price
        except:
            raise ValueError(f"Unable to normalize the price string: {price_str}")
    else:
        raise ValueError(f"Input must be a string, got {type(price_str)}")