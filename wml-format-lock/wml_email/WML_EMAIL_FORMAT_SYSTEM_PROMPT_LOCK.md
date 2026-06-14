# WML Email Format Lock — System-Prompt Style

Use this as the default outbound WML email format unless Ben explicitly overrides it.

## Non-negotiable footer
1. Every WML outbound evidence/submission email must end with the WML main-site logo image only.
2. Do not add extra text slogans under the logo. Do not add separate `WML Legal`, `WML`, or `WE MAKE LAW LEGAL` text beneath the logo. The logo asset itself is the identity mark.
3. Website must be clickable and visibly underlined: `https://wemakelawlegal.com`.
4. Email must be clickable and visibly underlined: `mailto:legal@wemakelawlegal.com`.
5. Footer contact structure after the logo:

```text
웹사이트: https://wemakelawlegal.com
이메일: legal@wemakelawlegal.com
제출 기준: [recipient/proceeding-specific submission standard]
```

6. Do not add defensive disclaimers in the footer unless Ben explicitly asks for one.
7. Do not use internal/archive phrasing such as `Record use`, `personal archive`, or `outside counsel review` in the visible footer unless Ben explicitly asks for it.

## Logo source
- Current locked logo asset: `templates/wml_email/wml-main-site-logo.png`. Email HTML uses public image URL so Gmail/browser can render it: `https://wemakelawlegal.com/assets/wml-source/wml-source-10.png?v=source-mark-20260602`.
- Source identity: WML main site logo from `https://wemakelawlegal.com/assets/wml-source/wml-source-10.png`.

## Email body rule
- Body can be Korean, English, or mixed depending on recipient.
- Keep the body concise and issuer-facing.
- State transaction anchor, requested relief, attached packet, and requested next action.
- Do not bury the ask below the footer.
- Do not send until Ben visually verifies recipient, subject, body, footer/logo, and attachment.

## Submission email default template
Recipient: `[recipient email confirmed from source]`
Subject default: `[recipient/proceeding] [case name] [requested relief]`
Attachment default: `[email-ready WML packet PDF]`
Never infer or alter recipient characters. If the address comes from screenshot/SMS/OCR/ASR, verify exact characters before send.

## Browser/send rule
Draft first. Verify visually. Send only after Ben says to send.
