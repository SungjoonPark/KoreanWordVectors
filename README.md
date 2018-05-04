# Word Vector Representation for Korean: Evaluation Set
**Subword-level Word Vector Representations for Korean**<br/>
*Sungjoon Park, Jeongmin Byun, Sion Baek, Yongseok Cho, Alice Oh*<br/>
*Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL 2018)*<br/>

## Abstract
Research on distributed word representations is focused on widely-used languages such as English. Although the same methods can be used for other languages, language-specific knowledge can enhance the accuracy and richness of word vector representations. In this paper, we look at improving distributed word representations for Korean using knowledge about the unique linguistic structure of Korean. Specifically, we decompose Korean words into the jamo-level, beyond the character-level, allowing a systematic use of subword information. To evaluate the vectors,w e develop Korean test sets for word similarity and analogy and make them publicly available. The results show that our simple method outperforms word2vec and character-level Skip-Grams on semantic and syntactic similarity and analogy tasks and contributes positively toward down-stream NLP tasks such as sentiment analysis.


## Dataset
We open our evaluation dataset for Korean word vectors. Details are described below. We plan to develop more evaluation sets for Korean NLP communities, so any comments for theses sets or collaboration for constructing other sets are welcome!

## 1. WS-353 for word similarity (Korean)
+  2 graduate students translated original (English) set.
+ 14 native Korean speakers participated in evaluation of the set.
+ Excluded the minimum and maximum scores and compute the mean of the rest of the scores.
+ .82 correlation with original English set.
+ Some of words are replaced by more familiar words to Korean. ( e.g.) Arafat -> 안중근 )

## 2. Word Analogies (Korean)
+ 10,000 items. 5,000 for semantic and 5,000 syntactic items.
+ 5 categories for semantic and syntactic features.
+ Each category contains 1,000 items.
+ **Syntactic Features (with an example)** :
    + Case : 자동차 자동차를 인터넷 인터넷을
    + Tense  가다 갔다 공부하다 공부했다
    + Voice  갈다 갈리다 거래하다 거래되다
	+ Verb form  가다 가고 놓다 놓고
	+ Honorific  가다 가시다 공부하다 공부하시다
+	**Semantic Features (with an example)**:
	+ Capital-countries 아테네 그리스 바그다드 이라크
	+ male-female 남자 여자 아버지 어머니
	+ name-nationality 간디 인도 나폴레옹 프랑스
	+ country-language 아르헨티나 스페인어 미국 영어
	+ misc  개 강아지 소 송아지

## Change Log
05-04-18 : Initial upload of datasets. version 1.0
