# CLAUDE.md — Blog cá nhân: vietthuynguyen.com

## Tổng quan project

Blog cá nhân về **AI trong thương mại điện tử**, viết bởi Viet Thuy Nguyen.
Mục tiêu: trở thành nguồn tài nguyên thực chiến hàng đầu tiếng Việt về ứng dụng AI cho seller và người vận hành ecom.

- **Domain:** vietthuynguyen.com  
- **Platform:** WordPress  
- **Ngôn ngữ:** Tiếng Việt  
- **Tần suất đăng:** 1 bài/ngày  

---

## Độc giả mục tiêu

**Primary:** Seller / chủ shop đang bán hàng online (Shopee, TikTok Shop, Facebook Commerce)

**Profile cụ thể:**
- Đang vận hành shop 1-10 người
- Biết dùng smartphone, thành thạo các app bán hàng cơ bản
- Chưa có background kỹ thuật sâu về AI
- Mục tiêu: tăng doanh thu, tiết kiệm thời gian, tự động hóa việc lặp lại
- Pain points: viết content mất thời gian, không biết chọn tool AI nào, sợ AI phức tạp

**Câu hỏi độc giả thường xuyên đặt ra:**
- "AI có thể làm thay được việc này không?"
- "Dùng tool nào tốt nhất cho Shopee?"
- "Bao lâu thì thấy kết quả?"

---

## Tone & Voice

**Nguyên tắc cốt lõi:** Viết như người trong nghề chia sẻ với đồng nghiệp — không phải giáo viên dạy học trò.

- **Thẳng thắn, thực chiến** — đi thẳng vào how-to, tránh dẫn dắt dài
- **Không lý thuyết học thuật** — không giải thích AI là gì nếu không cần thiết
- **Dùng ví dụ cụ thể** — luôn có ví dụ sát ngành ecom/thời trang Việt Nam
- **Ngắn gọn, có cấu trúc** — heading rõ ràng, đoạn ngắn, bullet khi cần
- **Tránh:** sáo rỗng, câu mở đầu kiểu "Trong thời đại 4.0...", kết bài chung chung

**Ví dụ tone đúng:**
> "Để viết 10 caption Shopee trong 5 phút, bạn cần làm đúng 3 bước sau..."

**Ví dụ tone sai:**
> "Trí tuệ nhân tạo đang mở ra cơ hội vô hạn cho doanh nghiệp Việt Nam..."

---

## Loại bài viết

### 1. How-to / Tutorial (ưu tiên cao nhất)
- Hướng dẫn dùng AI cho task cụ thể: viết listing, trả lời review, phân tích đối thủ, chạy ads...
- Format: step-by-step, có screenshot hoặc ví dụ thực tế
- Độ dài: 800–1.500 từ

### 2. Case Study
- Phân tích shop/brand thực tế đã dùng AI, kết quả cụ thể (số liệu)
- Format: bối cảnh → vấn đề → giải pháp AI → kết quả → bài học
- Độ dài: 1.000–2.000 từ

---

## Cấu trúc thư mục

```
blogcanhan/
├── CLAUDE.md               # File này
├── posts/
│   ├── drafts/             # Bài đang viết
│   ├── ready/              # Bài đã xong, chờ đăng
│   └── published/          # Bài đã đăng (lưu bản gốc)
├── research/               # Notes research, dữ liệu thu thập
├── seo/
│   ├── keywords.md         # Danh sách keyword đang target
│   └── internal-links.md   # Bản đồ internal linking
└── templates/
    ├── how-to.md           # Template bài how-to
    └── case-study.md       # Template bài case study
```

---

## SEO Guidelines

- **Target keyword** phải xuất hiện trong: title, H1, đoạn đầu tiên, ít nhất 1 H2, meta description
- **Title format:** `[Keyword chính] — [Benefit cụ thể] | vietthuynguyen.com`
- **Meta description:** 150–160 ký tự, có CTA ngầm
- **Slug:** tiếng Việt không dấu, dùng dấu `-`, ngắn gọn (3–6 từ)
- **Internal link:** mỗi bài tối thiểu 2 internal link đến bài liên quan
- **Image alt text:** mô tả rõ nội dung ảnh + keyword nếu tự nhiên

---

## Workflow tạo bài

```
1. Chọn topic → Research & outline (Claude hỗ trợ)
2. Xác nhận outline → Viết draft (Claude viết)
3. Review draft → Chỉnh sửa
4. SEO check → Tối ưu title, meta, keyword density
5. Move sang posts/ready/ → Schedule đăng WordPress
6. Sau khi đăng → Move sang posts/published/
```

---

## Vai trò của Claude trong project này

Claude đóng vai **biên tập viên + content strategist** của blog:

| Task | Chi tiết |
|------|----------|
| **Research & outline** | Tìm angle mới, phân tích topic, lập outline trước khi viết |
| **Viết draft** | Draft hoàn chỉnh theo tone và template đã định |
| **SEO optimize** | Keyword placement, meta description, internal link suggestion |
| **Quản lý file** | Tổ chức posts theo trạng thái, đặt tên file chuẩn |
| **Content calendar** | Gợi ý topic theo tuần, cân bằng how-to vs case study |

### Quy tắc khi Claude viết bài:
1. Luôn hỏi keyword target trước khi viết nếu chưa có
2. Mở bài bằng pain point hoặc kết quả cụ thể — không mở bằng định nghĩa
3. Mỗi section H2 phải có ít nhất 1 ví dụ hoặc action cụ thể
4. Kết bài bằng CTA rõ ràng (comment, thử tool, đọc bài tiếp theo)
5. Không dùng từ: "trong thời đại", "không thể phủ nhận", "chìa khóa thành công"

---

## Đặt tên file

```
YYYY-MM-DD_[slug-bai-viet].md
Ví dụ: 2026-05-12_dung-chatgpt-viet-listing-shopee.md
```

---

## Keywords đang target (seed list)

- AI viết content Shopee
- ChatGPT cho seller
- Công cụ AI bán hàng online
- Tự động hóa Shopee bằng AI
- AI phân tích đối thủ ecom
- Viết caption bán hàng bằng AI
- AI cho TikTok Shop Việt Nam

---

## Ghi chú vận hành

- **WordPress login:** quản lý qua wp-admin (Claude không truy cập trực tiếp)
- **Ảnh bài viết:** tạo bằng Canva hoặc AI image gen, lưu vào WordPress media
- **Lịch đăng:** ưu tiên 7:00–9:00 sáng (giờ VN) để catch traffic buổi sáng
- **Phân phối:** sau khi đăng → share Facebook Page + TikTok caption tóm tắt
