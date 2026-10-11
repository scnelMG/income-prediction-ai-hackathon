# 소득 예측 AI 해커톤

소득 예측 회귀 모델을 탐색하고, CatBoost 기반의 최종 제출 파일을 생성한 프로젝트입니다. 이 저장소는 재현 가능한 분석 코드와 실행 방법만 담는 GitHub 공개본입니다.

## 공개 저장소 구성

| 경로 | GitHub 공개 여부 | 내용 |
| --- | --- | --- |
| `notebooks/` | 포함 | 실행 출력과 셀 실행 번호를 제거한 EDA·모델링 코드 |
| `data/raw/` | 제외 | 학습·테스트·제출 형식 원본 데이터의 로컬 위치 |
| `outputs/` | 제외 | 모델 실행으로 생성되는 제출 파일 위치 |
| `drive_upload/` | 제외 | 원본 전체를 보관하는 Drive 업로드용 ZIP |
| 루트 원본 파일 | 제외 | 원본 노트북, 제출 CSV, 발표 자료, 학습 로그 |

원본 자료 전체는 로컬 `drive_upload/`의 제한된 Drive 업로드용 ZIP에 보관합니다. 데이터 재배포 권한과 개인정보 여부가 확인되기 전에는 GitHub에 추가하지 않습니다. 상세 기준은 [PUBLICATION_POLICY.md](PUBLICATION_POLICY.md)를 따릅니다.

## 노트북 형식 검증

```bash
python -m pip install -r requirements-check.txt
python scripts/validate_notebooks.py
```

CI는 두 노트북의 JSON·Jupyter 스키마를 검사하며, 누락된 셀 ID 등의 경고도 실패로 처리합니다. 비공개 원천 데이터를 사용하는 분석 셀은 실행하지 않으므로 모델 성능 재현 검증과는 구분됩니다.

## 실행 환경

Python 3.9 이상 환경에서 아래를 설치합니다.

```bash
python -m pip install -r requirements.txt
```

아래 파일을 `data/raw/`에 배치한 뒤 노트북을 실행합니다. 이 파일들은 공개 저장소에 포함하지 않습니다.

- `train.csv`
- `test.csv`
- `sample_submission.csv`

| 노트북 | 목적 | 결과 |
| --- | --- | --- |
| `notebooks/01_eda.ipynb` | 변수 분포와 특성 관계 탐색 | 탐색 결과 확인 |
| `notebooks/02_modeling_and_submission.ipynb` | 전처리, CatBoost 모델 학습, 예측 | `outputs/`에 제출 CSV 생성 |

## GitHub 업로드 전 확인

```powershell
git status --ignored
git add README.md .gitignore PUBLICATION_POLICY.md requirements.txt notebooks data/raw/.gitkeep outputs/.gitkeep
git diff --cached --stat
```

다음 항목은 GitHub에 추가하지 않습니다.

- 원본·중간·결과 CSV와 제출 파일
- 실행 출력이 남아 있는 원본 노트북과 CatBoost 로그
- 발표 자료, 대회 제출본, 별도 기업 재무 데이터 분석 자료
- 외부 서비스 키, 계정 정보, 개인정보 또는 재배포 권한이 불명확한 자료

## 데이터 출처와 한계

대회 데이터의 이용 범위와 재배포 조건은 대회 규정 및 원 데이터 제공자의 라이선스를 기준으로 별도 확인해야 합니다. 모델 성능과 예측 결과는 실행 환경, 전처리, 무작위 시드에 따라 달라질 수 있습니다.
