# WML Locked Format Automation Memory

Use this as durable memory for future WML Legal evidence packets and submission emails.

## Live object
When Ben asks to prepare a WML dispute/evidence packet, the object is not generic document design. The object is:

> legal-team style evidence organization + issuer/platform review packet + visually locked WML email footer + verifiable source evidence.

## Default packet route
1. Lock the transaction / event / incident anchor.
2. Separate main claim from appendix/supporting noise.
3. Build the main packet first: transaction, requested relief, chronology, service/incident records, impact, standards for review.
4. Build source-record index second.
5. Add real source captures third when visual proof is needed.
6. Put the final WML outro last.
7. Verify `Submission Packet Complete` appears only once and only on the last page.
8. Produce an email-ready PDF under Gmail attachment limits when needed.
9. Draft the WML email with locked footer/logo/link rules.
10. Do not send until Ben visually verifies recipient, subject, body, footer/logo, and attachment.

## PDF format lock
- Intro/cover first.
- Body pages use WML small header logo, header title, footer, and page number.
- Main packet precedes source-record index.
- Source-record index precedes source captures.
- Source captures precede the final outro.
- The final outro must be true terminal page.
- `Submission Packet Complete` must not appear in the middle.
- No material appears after the outro.
- Legal-team typography: serious, organized, not casual, not chatbot-like.
- Avoid hollow pages. If a paragraph is short, pair related short paragraphs on the same page. If a page is intentionally sparse, it must be cover/outro/source-image logic, not accidental emptiness.
- Do not split one same-topic heading into duplicate separated fragments. Example failure: splitting `6 MacBook Pro repair/service episodes` away from its own paragraph.
- Source geometry/proof outranks generative aesthetics.
- Never create AI-looking fake email cards as evidence. Use actual source pixels or clearly labeled summaries/indexes.

## Email format lock
- Footer uses only the WML main-site logo image at identity position.
- Do not add extra `WML Legal`, `WML`, or `WE MAKE LAW LEGAL` text below the logo.
- Website link must be clickable: `https://wemakelawlegal.com`.
- Email link must be clickable: `mailto:legal@wemakelawlegal.com`.
- Footer visible lines stay lean:
  - `웹사이트: https://wemakelawlegal.com`
  - `이메일: legal@wemakelawlegal.com`
  - `제출 기준: [specific review/submission standard]`
- No defensive disclaimer in footer unless Ben explicitly asks.
- No `Record use`, `personal archive`, or `outside counsel review` footer language unless Ben explicitly asks.
- Draft in Safari/Gmail when Ben has logged in there. Do not use a different account/tool if the live sending surface is Safari Gmail.
- Visual gate first: Ben must see recipient, subject, body, logo/footer, links if possible, and attachment before send.

## Case-specific data boundary
- Keep recipient emails, card details, transaction records, raw Gmail captures, and private dispute PDFs out of this public template repository.
- Store case-specific facts only in private workspaces or private repositories unless Ben explicitly chooses public disclosure.
- For every new matter, lock the recipient and transaction facts from source records before drafting or sending.

## Future reuse instruction
If Ben says any of these:
- `저장한 WML 포맷으로 써`
- `연구 저장한 그 포맷`
- `법률팀 톤으로 PDF 뽑아`
- `인트로/아웃트로 고정`
- `WML 이메일 푸터 붙여`

then load this memory plus:
- `templates/wml_pdf_packet_format/WML_PACKET_FORMAT_SYSTEM_PROMPT_LOCK.md`
- `templates/wml_email/WML_EMAIL_FORMAT_SYSTEM_PROMPT_LOCK.md`
- `templates/wml_email/WML_EMAIL_FOOTER_LOCK.html`
- `templates/WML_FORMAT_LOCK_MANIFEST.json`

and apply the locked architecture before generating new content.
