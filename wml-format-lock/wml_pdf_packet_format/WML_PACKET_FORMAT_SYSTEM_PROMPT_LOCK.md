# WML PDF Packet Format Lock — System-Prompt Style

Use this as the default WML issuer/evidence packet format unless Ben explicitly replaces it.

## Fixed packet architecture
1. Intro/cover page first.
2. Body pages with WML small header logo, issuer/document title, footer, and page numbers.
3. Main legal/evidence narrative before appendices.
4. Source-record index before raw/source captures.
5. Raw/source capture appendix before closing page.
6. Outro/closing page must be the true final page.

## Hard outro rule
- `Submission Packet Complete` appears only once.
- It must be the last page of the PDF.
- No evidence, appendix, source capture, transcript, or extra material may appear after the outro.

## Evidence integrity rule
- Do not create fake email-card evidence.
- Do not reconstruct Gmail records as generated screenshots.
- If email evidence is included visually, use actual source pixels or explicitly label it as an index/summary.
- Generated/retyped summaries can guide the reader but cannot masquerade as original proof.

## Visual density rule
- Legal-team tone.
- Professional typography.
- No half-empty repeated pages unless the page is cover/outro or source image page.
- Short subheading + same-topic paragraph stay together; do not split identical concepts across separate pages.
- Keep enough paragraph spacing for readability but avoid hollow pages.

## Current locked sample
`templates/locked_samples/WML_FORMAT_LOCK_SAMPLE_Apple_Issuer_Review_Packet_OUTRO_LOCKED_2026-06-14.pdf`

## Current final send version
`outputs/WML_Apple_MacBook_Pro_Vision_Pro_Issuer_Review_Packet_EMAIL_READY_2026-06-14.pdf`

## Final QA gate
Before delivery, verify:
- Page count.
- `Submission Packet Complete` only appears on final page.
- Website link and mailto link work on closing page when possible.
- Source appendix precedes outro.
- No `Draft`, no `partial refund`, no generated-email evidence language unless explicitly quarantined.
