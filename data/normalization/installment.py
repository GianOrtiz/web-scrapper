import re

def normalize_installment(installment_text):
    if installment_text is None:
        return None

    # Remove non-breaking spaces from the MagazineLuiza data.
    text = installment_text.replace('\xa0', ' ').strip()

    # Default data. 
    total_amount = None
    installments = None
    amount_per_installment = None

    # Regex for extracting total amount.
    total_match = re.search(r'R\$\s*([\d.,]+)', text)
    if total_match:
        total_amount = float(total_match.group(1).replace('.', '').replace(',', '.'))

    # Regex for extracting installments and per installments amount.
    installment_match = re.search(r'(\d+)[x|vezes|parcelas]?.*?R\$\s*([\d.,]+)', text, re.IGNORECASE)
    if installment_match:
        installments = int(installment_match.group(1))
        amount_per_installment = float(installment_match.group(2).replace('.', '').replace(',', '.'))

    # Single payment cases.
    single_payment_match = re.search(r'at[eé]\s*1x\s*de\s*R\$\s*([\d.,]+)', text, re.IGNORECASE)
    if single_payment_match and installments is None:
        installments = 1
        amount_per_installment = float(single_payment_match.group(1).replace('.', '').replace(',', '.'))

    return {
        "total_amount": total_amount,
        "installments": installments,
        "amount_per_installment": amount_per_installment,
    }
