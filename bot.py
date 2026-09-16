import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configura il logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# === QUI METTEREMO LE PREDIZIONI REALI ===
def get_prediction(match_text: str) -> str:
    """
    Funzione placeholder.
    Più avanti la sostituiamo con il modello vero.
    """
    match_text = match_text.lower().strip()
    
    # Esempi di risposta finta (da sostituire)
    if "inter" in match_text and "milan" in match_text:
        return (
            "🔥 *Derby di Milano*\n\n"
            "Probabilità:\n"
            "• Inter: 48%\n"
            "• Pareggio: 27%\n"
            "• Milan: 25%\n\n"
            "Over 2.5: 58%\n"
            "BTTS: 61%\n"
            "Score più probabile: 1-1 / 2-1"
        )
    
    return (
        f"Hai chiesto predizione per: *{match_text}*\n\n"
        "Al momento uso un modello base.\n"
        "Scrivi ad esempio:\n"
        "• Inter - Milan\n"
        "• predizioni giornata\n"
        "• Champions oggi"
    )

# Comandi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ciao! 👋 Sono la tua AI personale di predizioni calcistiche.\n\n"
        "Cosa puoi fare:\n"
        "• Scrivi una partita (es. *Inter - Milan*)\n"
        "• /giornata → prossime partite importanti\n"
        "• /help → lista comandi\n\n"
        "Top 5 + Champions, Europa e Conference League."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Comandi disponibili:*\n\n"
        "/start – Avvia il bot\n"
        "/giornata – Prossime partite\n"
        "/help – Questo messaggio\n\n"
        "Oppure scrivi direttamente una partita:\n"
        "`Inter - Milan`\n"
        "`Real Madrid - Barcelona`\n"
        "`predizioni Champions`"
    )

async def giornata(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Placeholder – più avanti lo colleghiamo ai dati reali
    await update.message.reply_text(
        "📅 *Prossime partite importanti*\n\n"
        "Questa funzione arriverà a breve.\n"
        "Per ora scrivi pure le partite che ti interessano!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    prediction = get_prediction(text)
    await update.message.reply_text(prediction, parse_mode="Markdown")

def main():
    # Prende il token dalla variabile d'ambiente (più sicuro)
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Manca la variabile d'ambiente BOT_TOKEN")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("giornata", giornata))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot avviato...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
