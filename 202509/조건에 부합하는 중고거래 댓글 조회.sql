-- board 테이블에서 게시글 제목과 게시글 id를 조회 가능.
-- reply 테이블과 조인 후 댓글 id와 작성장, 내용, 작성일도 조회
-- 댓글 작성일 기준 오름차순 정렬, 작성일이 같다면 게시글 제목 기준 오름차순.
select b.title, b.board_id,
r.reply_id, r.writer_id, r.contents, date_format(r.created_date, '%Y-%m-%d') as created_date
from used_goods_board as b
inner
join used_goods_reply as r
on r.board_id = b.board_id
where b.created_date >= '2022-10-01'
and b.created_date < '2022-11-01'      
order 
by r.created_date asc, b.title asc