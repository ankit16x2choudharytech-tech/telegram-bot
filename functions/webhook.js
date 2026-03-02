export async function onRequest(context) {
  if (context.request.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405 });
  }

  const BOT_TOKEN = context.env.BOT_TOKEN;
  const WEBSITE_LINK = "https://yourwebsite.com";

  const update = await context.request.json();

  if (!update.message) {
    return new Response("OK");
  }

  const chatId = update.message.chat.id;
  const text = update.message.text;

  let reply = "";

  if (text === "/start") {
    reply = "Choose language:\nEnglish\nHindi";
  }

  if (text === "English") {
    reply = "Your online service website link is here:\n" + WEBSITE_LINK;
  }

  if (text === "Hindi") {
    reply = "आपकी ऑनलाइन सर्विस वेबसाइट की लिंक यहां है:\n" + WEBSITE_LINK;
  }

  if (reply !== "") {
    await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: chatId,
        text: reply,
      }),
    });
  }

  return new Response("OK");
}