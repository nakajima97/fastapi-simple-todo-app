```mermaid
erDiagram

tasks {
  bigint id PK
  string title "タイトル"
  text description "詳細"
  tinyint finished_at "完了済み"
  datetime created_at "作成日"
}
```