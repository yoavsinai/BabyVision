# Detailed Evaluation Results: runs/baseline

## 📊 Summary Statistics
```text
Overall Average Accuracy: 0.1108 ± 0.0117

Type-wise Average Accuracy:
  Fine-grained Discrimination: 0.1084 ± 0.0190
  Spatial Perception: 0.1392 ± 0.0137
  Visual Pattern Recognition: 0.0980 ± 0.0000
  Visual Tracking: 0.0924 ± 0.0316

Subtype-wise Average Accuracy:
  1Fine-grained Discrimination/2D Pattern Completion: 0.4333 ± 0.0236
  1Fine-grained Discrimination/Count Clusters: 0.1296 ± 0.0693
  1Fine-grained Discrimination/Count Same Patterns: 0.0095 ± 0.0135
  1Fine-grained Discrimination/Find the different: 0.0000 ± 0.0000
  1Fine-grained Discrimination/Find the same: 0.0000 ± 0.0000
  1Fine-grained Discrimination/Find the shadow: 0.0725 ± 0.0205
  1Fine-grained Discrimination/Pattern and Color Completion: 0.2167 ± 0.0236
  1Fine-grained Discrimination/Reconstruction: 0.0238 ± 0.0337
  2Visual Tracking/Connect the lines: 0.1053 ± 0.0430
  2Visual Tracking/Lines Observation: 0.0000 ± 0.0000
  2Visual Tracking/Maze: 0.1833 ± 0.0624
  2Visual Tracking/Metro map: 0.0278 ± 0.0393
  2Visual Tracking/Recognize numbers and letters: 0.0725 ± 0.0205
  3Spatial Perception/3D Cube Unfold: 0.0278 ± 0.0393
  3Spatial Perception/3D Pattern Completion: 0.3148 ± 0.0693
  3Spatial Perception/3D Views: 0.1111 ± 0.0524
  3Spatial Perception/Count 3D blocks: 0.1212 ± 0.0214
  3Spatial Perception/Paper Folding: 0.0833 ± 0.0000
  4Visual Pattern Recognition/Logic Patterns: 0.0476 ± 0.0673
  4Visual Pattern Recognition/Mirroring Patterns: 0.0667 ± 0.0471
  4Visual Pattern Recognition/Overlay Patterns: 0.0980 ± 0.0277
  4Visual Pattern Recognition/Rotation Patterns: 0.2000 ± 0.0816
```

## 📝 Detailed Task-wise Results
Total evaluated tasks: **388**

| Task ID | Type / Subtype | Ground Truth | Pass 1 Ans (Judge) | Pass 2 Ans (Judge) | Pass 3 Ans (Judge) | Accuracy |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 445 | Fine-grained Discrimination / Find the different | (4,7) | `(4,2)` (❌) | `(5,5)` (❌) | `(2,1)` (❌) | **0.0%** |
| 464 | Fine-grained Discrimination / Find the different | (5,9) | `(4, 5)` (❌) | `(8, 10)` (❌) | `N/A` (❌) | **0.0%** |
| 507 | Fine-grained Discrimination / Find the different | (5,7) | `(4,7)` (❌) | `(4, 7)` (❌) | `(4,6)` (❌) | **0.0%** |
| 525 | Fine-grained Discrimination / Find the different | (7,8) | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 534 | Fine-grained Discrimination / Find the different | (6,12) | `(13, 10)` (❌) | `(3, 12)` (❌) | `N/A` (❌) | **0.0%** |
| 638 | Fine-grained Discrimination / Find the different | Row 4 Column 17 | `Row 15 Column 12` (❌) | `N/A` (❌) | `Row 12 Column 9` (❌) | **0.0%** |
| 779 | Fine-grained Discrimination / Find the different | (10, 9) | `(7, 5)` (❌) | `(4, 1)` (❌) | `(3, 6)` (❌) | **0.0%** |
| 879 | Fine-grained Discrimination / Find the different | 10,5 | `(15,12)` (❌) | `(15,10)` (❌) | `(14,6)` (❌) | **0.0%** |
| 910 | Fine-grained Discrimination / Find the different | 9,5 | `N/A` (❌) | `3,7` (❌) | `6,9` (❌) | **0.0%** |
| 984 | Fine-grained Discrimination / Find the different | (6,10) | `(5,12)` (❌) | `(5,10)` (❌) | `(5,11)` (❌) | **0.0%** |
| 986 | Fine-grained Discrimination / Find the different | (11,4) | `N/A` (❌) | `N/A` (❌) | `(5, \text{any column})` (❌) | **0.0%** |
| 988 | Fine-grained Discrimination / Find the different | (9,7) | `(17,10)` (❌) | `(8,10)` (❌) | `(12,10)` (❌) | **0.0%** |
| 4152 | Fine-grained Discrimination / Find the different | (7,2) | `N/A` (❌) | `N/A` (❌) | `(7,10)` (❌) | **0.0%** |
| 6161 | Fine-grained Discrimination / Find the different | (7,8) | `(3,10)` (❌) | `N/A` (❌) | `(1,10)` (❌) | **0.0%** |
| 6164 | Fine-grained Discrimination / Find the different | (9,2) | `N/A` (❌) | `N/A` (❌) | `(2,6)` (❌) | **0.0%** |
| 6165 | Fine-grained Discrimination / Find the different | 6-7 | `2-2` (❌) | `N/A` (❌) | `No different animal found` (❌) | **0.0%** |
| 437 | Fine-grained Discrimination / Find the same | 1-7,2-9,3-10,4-8,6-11 | `1-8, 2-5` (❌) | `1-10, 2-3` (❌) | `1-2, 3-4` (❌) | **0.0%** |
| 462 | Fine-grained Discrimination / Find the same | D | `A` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 469 | Fine-grained Discrimination / Find the same | 2-7 | `1-2` (❌) | `2-5` (❌) | `2-5` (❌) | **0.0%** |
| 475 | Fine-grained Discrimination / Find the same | (1,3)-(3,1) | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 476 | Fine-grained Discrimination / Find the same | 4-11 | `1-3` (❌) | `1-4` (❌) | `1-11` (❌) | **0.0%** |
| 478 | Fine-grained Discrimination / Find the same | 2,3,6,7,10 | `2,3,4,5,6,7,8,9,10` (❌) | `2,3,4,5,6,7,8,9,10` (❌) | `None` (❌) | **0.0%** |
| 498 | Fine-grained Discrimination / Find the same | BG,CE,DF | `N/A` (❌) | `AB,CD,EG` (❌) | `AB,CD,EG` (❌) | **0.0%** |
| 522 | Fine-grained Discrimination / Find the same | E | `A` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 617 | Fine-grained Discrimination / Find the same | C | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 626 | Fine-grained Discrimination / Find the same | Second row third column | `Row 1, Column 4` (❌) | `Row 2, Column 4` (❌) | `N/A` (❌) | **0.0%** |
| 635 | Fine-grained Discrimination / Find the same | 9-12 | `No pairs` (❌) | `No pairs` (❌) | `N/A` (❌) | **0.0%** |
| 651 | Fine-grained Discrimination / Find the same | 4-11 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 711 | Fine-grained Discrimination / Find the same | (2-1)-(3-3) | `(1-1)-(2-1)` (❌) | `(1-1)-(1-2)` (❌) | `(1-1)-(2-1)` (❌) | **0.0%** |
| 720 | Fine-grained Discrimination / Find the same | 12 | `N/A` (❌) | `None` (❌) | `1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19...` (❌) | **0.0%** |
| 4698 | Fine-grained Discrimination / Find the same | 2D,6A,4B,1B,5C,1F | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5597 | Fine-grained Discrimination / Find the same | 2,4,5,6,7,9 | `2, 4, 5, 6, 7` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 7568 | Fine-grained Discrimination / Find the same | F | `B` (❌) | `B` (❌) | `A` (❌) | **0.0%** |
| 459 | Fine-grained Discrimination / Find the shadow | 1-4,3-12,5-10,7-2,9-6,11-8 | `N/A` (❌) | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | **0.0%** |
| 644 | Fine-grained Discrimination / Find the shadow | 1-6,2-5,3-8,4-11,5-12,6-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 826 | Fine-grained Discrimination / Find the shadow | 1-6,3-4,5-8,7-12,9-10,11-2 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4994 | Fine-grained Discrimination / Find the shadow | D | `B` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 4996 | Fine-grained Discrimination / Find the shadow | C | `None` (❌) | `None of the above` (❌) | `None` (❌) | **0.0%** |
| 4998 | Fine-grained Discrimination / Find the shadow | B | `C` (❌) | `B` (✅) | `C` (❌) | **33.3%** |
| 5001 | Fine-grained Discrimination / Find the shadow | Second row third column | `2, 2` (❌) | `1, 1` (❌) | `1, 1` (❌) | **0.0%** |
| 5004 | Fine-grained Discrimination / Find the shadow | Second row first column | `Row 1, Column 1` (❌) | `1, 1` (✅) | `2, 1` (✅) | **66.7%** |
| 5006 | Fine-grained Discrimination / Find the shadow | Row 1, Column 2 | `Any row and column, e.g., Row 1, Column 1` (❌) | `Row 2, Column 2` (❌) | `Any row and column` (❌) | **0.0%** |
| 5008 | Fine-grained Discrimination / Find the shadow | The second row, third column | `R2, C3` (✅) | `2, 1` (❌) | `Row 2, Column 2` (❌) | **33.3%** |
| 5009 | Fine-grained Discrimination / Find the shadow | Row 1 Column 3 | `N/A` (❌) | `1, 2` (❌) | `3, 3` (❌) | **0.0%** |
| 5011 | Fine-grained Discrimination / Find the shadow | Third row first column | `Row 3, Column 1` (✅) | `Row 3, Column 3` (❌) | `Row 3, Column 3` (❌) | **33.3%** |
| 5013 | Fine-grained Discrimination / Find the shadow | Third Row Second Column | `1, 1` (❌) | `1, 1` (❌) | `2, 1` (❌) | **0.0%** |
| 5016 | Fine-grained Discrimination / Find the shadow | 1-C,2-G,3-D,4-E,5-B,6-F,7-A | `N/A` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D, 5-E, 6-F, 7-G` (❌) | **0.0%** |
| 5018 | Fine-grained Discrimination / Find the shadow | The third row and first column | `First row, First column` (❌) | `Second row, left column` (❌) | `Row 1, Column 1` (❌) | **0.0%** |
| 5020 | Fine-grained Discrimination / Find the shadow | Second column, first one | `3, 2` (❌) | `No match` (❌) | `3, 2` (❌) | **0.0%** |
| 5022 | Fine-grained Discrimination / Find the shadow | The first row and second column | `3, 1` (❌) | `3, 1` (❌) | `Bottom row, second column` (❌) | **0.0%** |
| 5023 | Fine-grained Discrimination / Find the shadow | Second row second | `Row 4, Column 3` (❌) | `1, 3` (❌) | `4, 3` (❌) | **0.0%** |
| 5025 | Fine-grained Discrimination / Find the shadow | 1-G,2-D,3-A,4-F,6-B,7-E,8-H,9-C | `1-A, 2-B, 3-C, 4-D, 9-E, 6-F, 7-G, 8-H` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5026 | Fine-grained Discrimination / Find the shadow | 1-F,2-D,3-E,4-B,6-H,7-A,8-G,9-C | `N/A` (❌) | `1-E, 2-B, 3-C, 4-D, 6-H, 7-F, 8-G, 9-A` (❌) | `N/A` (❌) | **0.0%** |
| 5030 | Fine-grained Discrimination / Find the shadow | 1-F,2-G,3-D,4-B,6-C,7-H,8-A,9-E | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6504 | Fine-grained Discrimination / Find the shadow | 1-4,2-3,3-1,4-2 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6512 | Fine-grained Discrimination / Find the shadow | 1-7,2-8,3-6,4-10,5-9 | `N/A` (❌) | `N/A` (❌) | `1-7,2-6,3-10,4-9,5-8` (❌) | **0.0%** |
| 535 | Fine-grained Discrimination / Reconstruction | B | `C` (❌) | `A` (❌) | `C` (❌) | **0.0%** |
| 2353 | Fine-grained Discrimination / Reconstruction | C | `N/A` (❌) | `C` (✅) | `N/A` (❌) | **33.3%** |
| 5270 | Fine-grained Discrimination / Reconstruction | 2,3,5 | `1, 3` (❌) | `1,2,3,4` (❌) | `1, 2, 3, 4` (❌) | **0.0%** |
| 5271 | Fine-grained Discrimination / Reconstruction | 1,3,4 | `1,2,3` (❌) | `1,2,3,4,5` (❌) | `1, 4` (❌) | **0.0%** |
| 5274 | Fine-grained Discrimination / Reconstruction | 1,3,4,5 | `1, 2, 3, 4, 5` (❌) | `1, 2, 3, 4, 5` (❌) | `1,2,3,4` (❌) | **0.0%** |
| 5275 | Fine-grained Discrimination / Reconstruction | 2,3,4,5 | `1, 2, 3, 5` (❌) | `1, 2, 3, 5` (❌) | `1, 2, 4` (❌) | **0.0%** |
| 5276 | Fine-grained Discrimination / Reconstruction | 1,3,4,6,8 | `1, 2, 4` (❌) | `1, 2, 3, 4, 5, 6` (❌) | `2, 4` (❌) | **0.0%** |
| 5277 | Fine-grained Discrimination / Reconstruction | 1,2,4,5,8 | `N/A` (❌) | `N/A` (❌) | `1, 3, 5, 7, 8` (❌) | **0.0%** |
| 5339 | Fine-grained Discrimination / Reconstruction | 1-9, 2-8, 3-10, 4-6, 5-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6131 | Fine-grained Discrimination / Reconstruction | 1-B,2-C,3-D,4-A | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6134 | Fine-grained Discrimination / Reconstruction | 1-B,2-D,3-A,4-C | `N/A` (❌) | `1-B, 2-A, 3-C, 4-D` (❌) | `N/A` (❌) | **0.0%** |
| 6136 | Fine-grained Discrimination / Reconstruction | 1-C,2-D,3-A,4-B | `N/A` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6137 | Fine-grained Discrimination / Reconstruction | 1-D,2-A,3-B,4-C | `1-A, 2-B, 3-C, 4-D` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6273 | Fine-grained Discrimination / Reconstruction | A-6, B-3, C-4, D-1, E-2, F-5 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 457 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `B` (❌) | `A` (❌) | **0.0%** |
| 494 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 637 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 640 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `Choices: (B)` (❌) | `A` (✅) | **66.7%** |
| 673 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `B` (❌) | **66.7%** |
| 765 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `C` (❌) | **66.7%** |
| 876 | Fine-grained Discrimination / 2D Pattern Completion | B | `(B)` (✅) | `B` (✅) | `B` (✅) | **100.0%** |
| 3995 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4026 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 4104 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `A` (✅) | **33.3%** |
| 4133 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 4142 | Fine-grained Discrimination / 2D Pattern Completion | C | `D` (❌) | `C` (✅) | `C` (✅) | **66.7%** |
| 4173 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `B` (❌) | `C` (✅) | **33.3%** |
| 4188 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 4190 | Fine-grained Discrimination / 2D Pattern Completion | B | `B` (✅) | `C` (❌) | `C` (❌) | **33.3%** |
| 4386 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4399 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 4405 | Fine-grained Discrimination / 2D Pattern Completion | D | `C` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4415 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 4712 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `A` (❌) | `B)` (❌) | **0.0%** |
| 559 | Fine-grained Discrimination / Pattern and Color Completion | A | `N/A` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 628 | Fine-grained Discrimination / Pattern and Color Completion | C | `C` (✅) | `B` (❌) | `B` (❌) | **33.3%** |
| 633 | Fine-grained Discrimination / Pattern and Color Completion | B | `Choice (B)` (✅) | `A` (❌) | `Choice (B)` (✅) | **66.7%** |
| 639 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 645 | Fine-grained Discrimination / Pattern and Color Completion | A | `B` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 652 | Fine-grained Discrimination / Pattern and Color Completion | C | `C` (✅) | `C` (✅) | `N/A` (❌) | **66.7%** |
| 695 | Fine-grained Discrimination / Pattern and Color Completion | C | `B` (❌) | `B` (❌) | `A` (❌) | **0.0%** |
| 699 | Fine-grained Discrimination / Pattern and Color Completion | D | `A` (❌) | `B` (❌) | `D` (✅) | **33.3%** |
| 721 | Fine-grained Discrimination / Pattern and Color Completion | A | `B` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 790 | Fine-grained Discrimination / Pattern and Color Completion | D | `N/A` (❌) | `N/A` (❌) | `A` (❌) | **0.0%** |
| 792 | Fine-grained Discrimination / Pattern and Color Completion | C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1594 | Fine-grained Discrimination / Pattern and Color Completion | B | `D` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 4146 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `A` (❌) | `B` (❌) | **0.0%** |
| 4148 | Fine-grained Discrimination / Pattern and Color Completion | C | `B` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 4181 | Fine-grained Discrimination / Pattern and Color Completion | B | `D` (❌) | `B` (✅) | `C` (❌) | **33.3%** |
| 4768 | Fine-grained Discrimination / Pattern and Color Completion | 1-D,2-B,3-A,4-C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5123 | Fine-grained Discrimination / Pattern and Color Completion | Row 2, Column 3 | `1, 2` (❌) | `3, 2` (❌) | `2, 2` (❌) | **0.0%** |
| 5399 | Fine-grained Discrimination / Pattern and Color Completion | B | `B` (✅) | `B` (✅) | `B` (✅) | **100.0%** |
| 6206 | Fine-grained Discrimination / Pattern and Color Completion | 2,6,8 | `3,5,9` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 7858 | Fine-grained Discrimination / Pattern and Color Completion | B | `N/A` (❌) | `B` (✅) | `A` (❌) | **33.3%** |
| 4534 | Fine-grained Discrimination / Count Same Patterns | 14 | `13` (❌) | `17` (❌) | `16` (❌) | **0.0%** |
| 4536 | Fine-grained Discrimination / Count Same Patterns | 15 | `11` (❌) | `10` (❌) | `13` (❌) | **0.0%** |
| 4537 | Fine-grained Discrimination / Count Same Patterns | 13 | `8` (❌) | `9` (❌) | `9` (❌) | **0.0%** |
| 4540 | Fine-grained Discrimination / Count Same Patterns | 18 | `13` (❌) | `11` (❌) | `17` (❌) | **0.0%** |
| 4552 | Fine-grained Discrimination / Count Same Patterns | 54 | `31` (❌) | `59` (❌) | `33` (❌) | **0.0%** |
| 4553 | Fine-grained Discrimination / Count Same Patterns | 58 | `47` (❌) | `53` (❌) | `45` (❌) | **0.0%** |
| 4554 | Fine-grained Discrimination / Count Same Patterns | 42 | `23` (❌) | `23` (❌) | `17` (❌) | **0.0%** |
| 4556 | Fine-grained Discrimination / Count Same Patterns | 67 | `43` (❌) | `49` (❌) | `49` (❌) | **0.0%** |
| 4558 | Fine-grained Discrimination / Count Same Patterns | 54 | `44` (❌) | `48` (❌) | `46` (❌) | **0.0%** |
| 4560 | Fine-grained Discrimination / Count Same Patterns | 36 | `17` (❌) | `14` (❌) | `14` (❌) | **0.0%** |
| 4561 | Fine-grained Discrimination / Count Same Patterns | 38 | `26` (❌) | `26` (❌) | `19` (❌) | **0.0%** |
| 4562 | Fine-grained Discrimination / Count Same Patterns | 36 | `17` (❌) | `12` (❌) | `13` (❌) | **0.0%** |
| 4564 | Fine-grained Discrimination / Count Same Patterns | 32 | `17` (❌) | `16` (❌) | `16` (❌) | **0.0%** |
| 4566 | Fine-grained Discrimination / Count Same Patterns | 17 | `8` (❌) | `9` (❌) | `9` (❌) | **0.0%** |
| 4568 | Fine-grained Discrimination / Count Same Patterns | 34 | `20` (❌) | `23` (❌) | `16` (❌) | **0.0%** |
| 4571 | Fine-grained Discrimination / Count Same Patterns | 36 | `26` (❌) | `17` (❌) | `26` (❌) | **0.0%** |
| 5073 | Fine-grained Discrimination / Count Same Patterns | 23 | `N/A` (❌) | `18` (❌) | `0` (❌) | **0.0%** |
| 5074 | Fine-grained Discrimination / Count Same Patterns | 22 | `N/A` (❌) | `10` (❌) | `N/A` (❌) | **0.0%** |
| 5081 | Fine-grained Discrimination / Count Same Patterns | 18 | `10` (❌) | `12` (❌) | `12` (❌) | **0.0%** |
| 5082 | Fine-grained Discrimination / Count Same Patterns | 14 | `12` (❌) | `14` (✅) | `18` (❌) | **33.3%** |
| 5083 | Fine-grained Discrimination / Count Same Patterns | 24 | `12` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5084 | Fine-grained Discrimination / Count Same Patterns | 24 | `12` (❌) | `6` (❌) | `12` (❌) | **0.0%** |
| 5085 | Fine-grained Discrimination / Count Same Patterns | 18 | `15` (❌) | `16` (❌) | `14` (❌) | **0.0%** |
| 5086 | Fine-grained Discrimination / Count Same Patterns | 34 | `8` (❌) | `1` (❌) | `9` (❌) | **0.0%** |
| 5357 | Fine-grained Discrimination / Count Same Patterns | 8, 3, 7, 4, 5, 6 | `N/A` (❌) | `8,0,9,8,5,0` (❌) | `8,0,8,9,8,0` (❌) | **0.0%** |
| 5358 | Fine-grained Discrimination / Count Same Patterns | 7, 4, 5, 9, 2 | `8,7,6,6,3` (❌) | `9,9,8,9,3` (❌) | `7,8,6,8,3` (❌) | **0.0%** |
| 5638 | Fine-grained Discrimination / Count Same Patterns | 4 | `0` (❌) | `1` (❌) | `0` (❌) | **0.0%** |
| 5639 | Fine-grained Discrimination / Count Same Patterns | 4 | `1` (❌) | `0` (❌) | `1` (❌) | **0.0%** |
| 5640 | Fine-grained Discrimination / Count Same Patterns | 5 | `1` (❌) | `1` (❌) | `15` (❌) | **0.0%** |
| 5781 | Fine-grained Discrimination / Count Same Patterns | 5 | `36` (❌) | `18` (❌) | `16` (❌) | **0.0%** |
| 5786 | Fine-grained Discrimination / Count Same Patterns | 10 | `0` (❌) | `0` (❌) | `0` (❌) | **0.0%** |
| 6421 | Fine-grained Discrimination / Count Same Patterns | 7,6,2,7,9,5 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6436 | Fine-grained Discrimination / Count Same Patterns | 8,7,3,2 | `4,4,4,4` (❌) | `N/A` (❌) | `4,4,4,4` (❌) | **0.0%** |
| 6466 | Fine-grained Discrimination / Count Same Patterns | 5,6,5,8 | `3,5,5,4` (❌) | `4,5,5,4` (❌) | `5,7,5,5` (❌) | **0.0%** |
| 6475 | Fine-grained Discrimination / Count Same Patterns | 15,10,11,15 | `6,5,6,6` (❌) | `5,4,8,7` (❌) | `8,4,10,11` (❌) | **0.0%** |
| 496 | Fine-grained Discrimination / Count Clusters | 18 | `0` (❌) | `9` (❌) | `9` (❌) | **0.0%** |
| 4650 | Fine-grained Discrimination / Count Clusters | 19 | `18` (❌) | `18` (❌) | `17` (❌) | **0.0%** |
| 4652 | Fine-grained Discrimination / Count Clusters | 21 | `15` (❌) | `15` (❌) | `18` (❌) | **0.0%** |
| 4653 | Fine-grained Discrimination / Count Clusters | 9 | `6` (❌) | `7` (❌) | `7` (❌) | **0.0%** |
| 5107 | Fine-grained Discrimination / Count Clusters | 8 | `13` (❌) | `12` (❌) | `12` (❌) | **0.0%** |
| 5113 | Fine-grained Discrimination / Count Clusters | 10 | `11` (❌) | `11` (❌) | `12` (❌) | **0.0%** |
| 5114 | Fine-grained Discrimination / Count Clusters | 9 | `11` (❌) | `10` (❌) | `11` (❌) | **0.0%** |
| 5117 | Fine-grained Discrimination / Count Clusters | 8,7 | `13, 5` (❌) | `11,6` (❌) | `11, 5` (❌) | **0.0%** |
| 5119 | Fine-grained Discrimination / Count Clusters | 10 | `10` (✅) | `10` (✅) | `11` (❌) | **66.7%** |
| 5378 | Fine-grained Discrimination / Count Clusters | 6,3,5,5 | `1,1,1,1` (❌) | `1,1,1,1` (❌) | `N/A` (❌) | **0.0%** |
| 5455 | Fine-grained Discrimination / Count Clusters | 2+6+1+3=12 | `2+5+1+3=11` (❌) | `N/A` (❌) | `2+6+1+3=12` (✅) | **33.3%** |
| 5490 | Fine-grained Discrimination / Count Clusters | 8−5=3 | `6-4=2` (❌) | `6-4=2` (❌) | `6-4=2` (❌) | **0.0%** |
| 5492 | Fine-grained Discrimination / Count Clusters | 7−1=6 | `6-2=4` (❌) | `7-1=6` (✅) | `6-1=5` (❌) | **33.3%** |
| 5795 | Fine-grained Discrimination / Count Clusters | 10,14,12 | `N/A` (❌) | `30` (❌) | `25` (❌) | **0.0%** |
| 6534 | Fine-grained Discrimination / Count Clusters | 1-2, 2-1, 3-4, 4-3 | `N/A` (❌) | `N/A` (❌) | `1-4, 3-3` (❌) | **0.0%** |
| 6555 | Fine-grained Discrimination / Count Clusters | > | `<` (❌) | `>` (✅) | `=` (❌) | **33.3%** |
| 6556 | Fine-grained Discrimination / Count Clusters | < | `<` (✅) | `<` (✅) | `>` (❌) | **66.7%** |
| 6557 | Fine-grained Discrimination / Count Clusters | = | `<` (❌) | `<` (❌) | `<` (❌) | **0.0%** |
| 666 | Visual Tracking / Maze | B | `B` (✅) | `B` (✅) | `(B)` (✅) | **100.0%** |
| 674 | Visual Tracking / Maze | E | `E` (✅) | `A` (❌) | `N/A` (❌) | **33.3%** |
| 817 | Visual Tracking / Maze | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 980 | Visual Tracking / Maze | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 982 | Visual Tracking / Maze | A | `(B)` (❌) | `Right upper inlet` (✅) | `B` (❌) | **33.3%** |
| 983 | Visual Tracking / Maze | A | `A` (✅) | `Answer: (A)` (✅) | `Choice (B)` (❌) | **66.7%** |
| 1306 | Visual Tracking / Maze | B | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 1651 | Visual Tracking / Maze | B | `A` (❌) | `Answer: (B)` (✅) | `A` (❌) | **33.3%** |
| 3782 | Visual Tracking / Maze | C | `N/A` (❌) | `Cannot be determined` (❌) | `B` (❌) | **0.0%** |
| 5124 | Visual Tracking / Maze | 39 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5127 | Visual Tracking / Maze | 59 | `12` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5128 | Visual Tracking / Maze | 50 | `14` (❌) | `N/A` (❌) | `16` (❌) | **0.0%** |
| 5130 | Visual Tracking / Maze | 57 | `N/A` (❌) | `13` (❌) | `16` (❌) | **0.0%** |
| 5131 | Visual Tracking / Maze | 53 | `N/A` (❌) | `23` (❌) | `N/A` (❌) | **0.0%** |
| 5133 | Visual Tracking / Maze | 51 | `N/A` (❌) | `29` (❌) | `N/A` (❌) | **0.0%** |
| 5136 | Visual Tracking / Maze | 27 | `17` (❌) | `21` (❌) | `18` (❌) | **0.0%** |
| 5139 | Visual Tracking / Maze | 38 | `N/A` (❌) | `N/A` (❌) | `12` (❌) | **0.0%** |
| 5140 | Visual Tracking / Maze | 52 | `13` (❌) | `6` (❌) | `12` (❌) | **0.0%** |
| 5142 | Visual Tracking / Maze | 52 | `14` (❌) | `22` (❌) | `20` (❌) | **0.0%** |
| 5143 | Visual Tracking / Maze | 55 | `N/A` (❌) | `19` (❌) | `N/A` (❌) | **0.0%** |
| 770 | Visual Tracking / Connect the lines | A-2,B-3,C-1 | `N/A` (❌) | `A-1, B-2, C-3` (❌) | `A-1, B-2, C-3` (❌) | **0.0%** |
| 1662 | Visual Tracking / Connect the lines | 4,2,6,5,7,3,1 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 2492 | Visual Tracking / Connect the lines | D | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 4327 | Visual Tracking / Connect the lines | 1-B,2-A,3-C | `1-A, 2-B, 3-C` (❌) | `1-A, 2-B, 3-C` (❌) | `1-A, 2-B, 3-C` (❌) | **0.0%** |
| 4329 | Visual Tracking / Connect the lines | 10,7,7 | `3, 6, 7` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4330 | Visual Tracking / Connect the lines | A - Blue, B - Yellow, C - Green | `A-blue, B-yellow, C-green` (✅) | `A-blue, B-yellow, C-green` (✅) | `N/A` (❌) | **66.7%** |
| 4332 | Visual Tracking / Connect the lines | 3-Gem,1-Fan,2-Crab,4-Skull | `a-gem,b-fan,c-crab,d-skull` (❌) | `a-gem,b-fan,c-crab,d-skull` (❌) | `a-gem,b-fan,c-crab,d-skull` (❌) | **0.0%** |
| 4337 | Visual Tracking / Connect the lines | 1-Skull #3, 2-Skull #2, 3-Diamond, 4-Skull #1 | `Line 1: Skull #1, Line 2: Diamond, Line 3: Skul...` (❌) | `Line 1: Skull #1, Line 2: Diamond, Line 3: Skul...` (❌) | `Line 1 $\rightarrow$ Skull #1, Line 2 $\rightar...` (❌) | **0.0%** |
| 4352 | Visual Tracking / Connect the lines | A-Circle, B-Triangle, C-Rectangle, D-Square, E-... | `Red-square, Blue-circle, Yellow-pentagram, Gree...` (✅) | `Red-square, Blue-circle, Yellow-pentagram, Gree...` (❌) | `Red-square, Blue-circle, Yellow-pentagram, Gree...` (❌) | **33.3%** |
| 5152 | Visual Tracking / Connect the lines | 1-S,2-N,3-O,4-W,5-M,6-A,7-N | `1-W,2-N,3-N,4-O,5-A,6-M,7-S` (❌) | `1-W,2-N,3-N,4-O,5-A,6-M,7-S` (❌) | `1-W,2-N,3-N,4-O,5-A,6-M,7-S` (❌) | **0.0%** |
| 5154 | Visual Tracking / Connect the lines | A-X,B-Y,C-Z,D-W | `A-W, B-X, C-Y, D-Z` (✅) | `A-W, B-X, C-Y, D-Z` (✅) | `A-W, B-X, C-Y, D-Z` (✅) | **100.0%** |
| 5156 | Visual Tracking / Connect the lines | 1-D,2-I,3-A,4-M,5-O,6-N,7-D | `1-A,2-N,3-D,4-D,5-O,6-I,7-M` (❌) | `1-A,2-N,3-D,4-D,5-O,6-I,7-M` (❌) | `1-A,2-N,3-D,4-D,5-O,6-I,7-M` (❌) | **0.0%** |
| 5161 | Visual Tracking / Connect the lines | 1-U,2-M,3-B,4-R,5-E,6-L,7-L,8-A | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | **0.0%** |
| 5164 | Visual Tracking / Connect the lines | 1-H,2-E,3-D,4-G,5-E,6-H,7-O,8-G | `1-E,2-H,3-O,4-E,5-G,6-G,7-H,8-D` (❌) | `1-E, 2-H, 3-O, 4-E, 5-G, 6-G, 7-H, 8-D` (❌) | `1-E,2-H,3-O,4-E,5-G,6-G,7-H,8-D` (❌) | **0.0%** |
| 5245 | Visual Tracking / Connect the lines | Still,waters,run,deep | `SALE, SEND, SURE, STAR` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5246 | Visual Tracking / Connect the lines | Better,late,than,never | `bear, heart, rent, late` (❌) | `bear, rent, tea, aven` (❌) | `N/A` (❌) | **0.0%** |
| 5247 | Visual Tracking / Connect the lines | Which,witch,is,which | `N/A` (❌) | `wish, whit, what, with` (❌) | `WHIW, CTC H, IWIH, IHS` (❌) | **0.0%** |
| 5248 | Visual Tracking / Connect the lines | Rolling,red,wagons | `ROG, RAG, ROW` (❌) | `ring, role, sand` (❌) | `RING, ROAD, LOW` (❌) | **0.0%** |
| 5249 | Visual Tracking / Connect the lines | Daddy,draws,doors | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 447 | Visual Tracking / Recognize numbers and letters | 2,N,Z,S | `A,N,Z,S` (❌) | `A,S,Z,S` (❌) | `A,S,Z,S` (❌) | **0.0%** |
| 520 | Visual Tracking / Recognize numbers and letters | G,4,D,6 | `4,C,D,6` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 542 | Visual Tracking / Recognize numbers and letters | 6,9,8 | `N/A` (❌) | `1, 1, 1` (❌) | `1, 2, 2` (❌) | **0.0%** |
| 543 | Visual Tracking / Recognize numbers and letters | 0,9,3 | `1,1,1` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 544 | Visual Tracking / Recognize numbers and letters | 3,6,2 | `No numbers are present in the image.` (❌) | `No numbers present` (❌) | `No numbers found` (❌) | **0.0%** |
| 545 | Visual Tracking / Recognize numbers and letters | 3,7,2 | `3, 3, 3` (❌) | `3` (❌) | `N/A` (❌) | **0.0%** |
| 665 | Visual Tracking / Recognize numbers and letters | D, 2, 4 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 671 | Visual Tracking / Recognize numbers and letters | C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 757 | Visual Tracking / Recognize numbers and letters | AN APPLE | `AN FELP` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1298 | Visual Tracking / Recognize numbers and letters | J, U, 3 | `W, 3` (❌) | `W, U, 3` (❌) | `W, U, 3` (❌) | **0.0%** |
| 1587 | Visual Tracking / Recognize numbers and letters | D,8,P,T | `O, S, P, A` (❌) | `D,S,B,A` (❌) | `D, S, B, T` (❌) | **0.0%** |
| 5227 | Visual Tracking / Recognize numbers and letters | 3,4,9 | `1, 2, 3` (❌) | `1, 2, 3` (❌) | `1, 2, 3` (❌) | **0.0%** |
| 5228 | Visual Tracking / Recognize numbers and letters | 3,4,5 | `3, 4, 5` (✅) | `3, 4, 5` (✅) | `2, 3, 4` (❌) | **66.7%** |
| 5229 | Visual Tracking / Recognize numbers and letters | 1,6,7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5238 | Visual Tracking / Recognize numbers and letters | 3,4,9 | `N/A` (❌) | `N/A` (❌) | `No numbers are present` (❌) | **0.0%** |
| 5239 | Visual Tracking / Recognize numbers and letters | 1,4,7 | `None` (❌) | `None` (❌) | `None` (❌) | **0.0%** |
| 5240 | Visual Tracking / Recognize numbers and letters | 2,5,8 | `1, 2, 5` (❌) | `No numbers are present` (❌) | `1, 5, 9` (❌) | **0.0%** |
| 5241 | Visual Tracking / Recognize numbers and letters | 2,5,9 | `1, 2, 9` (❌) | `1, 2, 5` (❌) | `1, 2, 9` (❌) | **0.0%** |
| 5242 | Visual Tracking / Recognize numbers and letters | 1,3,7 | `1, 3, 7` (✅) | `1, 3, 7` (✅) | `1, 3, 7` (✅) | **100.0%** |
| 5505 | Visual Tracking / Recognize numbers and letters | 2, 7, 5, 9 | `blue,green,red,yellow` (❌) | `B,G,R,Y` (❌) | `N/A` (❌) | **0.0%** |
| 5507 | Visual Tracking / Recognize numbers and letters | O, 8, N, Z | `N/A` (❌) | `N/A` (❌) | `8, s, N, Z` (❌) | **0.0%** |
| 6435 | Visual Tracking / Recognize numbers and letters | 3,6,1 | `Not enough information` (❌) | `No numbers found` (❌) | `N/A` (❌) | **0.0%** |
| 6509 | Visual Tracking / Recognize numbers and letters | 4, 6, 5, 5 | `1234` (❌) | `1, 2, 3, 4` (❌) | `X, \text{Loop}, \text{Segment}, \text{Square}` (❌) | **0.0%** |
| 8326 | Visual Tracking / Metro map | 6 | `4` (❌) | `N/A` (❌) | `2` (❌) | **0.0%** |
| 8327 | Visual Tracking / Metro map | 8 | `7` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8328 | Visual Tracking / Metro map | 11 | `10` (❌) | `4` (❌) | `2` (❌) | **0.0%** |
| 8329 | Visual Tracking / Metro map | 4 | `4` (✅) | `N/A` (❌) | `3` (❌) | **33.3%** |
| 8330 | Visual Tracking / Metro map | 8 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8331 | Visual Tracking / Metro map | 10 | `1` (❌) | `1` (❌) | `1` (❌) | **0.0%** |
| 8332 | Visual Tracking / Metro map | 9 | `3` (❌) | `2` (❌) | `1` (❌) | **0.0%** |
| 8339 | Visual Tracking / Metro map | 22 | `N/A` (❌) | `N/A` (❌) | `3` (❌) | **0.0%** |
| 8340 | Visual Tracking / Metro map | 8 | `0` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8341 | Visual Tracking / Metro map | 20 | `2` (❌) | `4` (❌) | `5` (❌) | **0.0%** |
| 8342 | Visual Tracking / Metro map | 12 | `N/A` (❌) | `2` (❌) | `3` (❌) | **0.0%** |
| 8343 | Visual Tracking / Metro map | 11 | `N/A` (❌) | `N/A` (❌) | `2` (❌) | **0.0%** |
| 8162 | Visual Tracking / Lines Observation | 15,13,12,10,9,9,9,8,8,7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8163 | Visual Tracking / Lines Observation | 17,16,12,12,11,11,9,5,4,3 | `N/A` (❌) | `N/A` (❌) | `15,14,11,10,7,4,3,3` (❌) | **0.0%** |
| 8164 | Visual Tracking / Lines Observation | 14,11,10,9,7,6,4,3 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8165 | Visual Tracking / Lines Observation | 25,7,7,6,6,5,4,4 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8166 | Visual Tracking / Lines Observation | 13,11,10,9,7,6,5,3 | `N/A` (❌) | `N/A` (❌) | `8,7,5,5,4` (❌) | **0.0%** |
| 8167 | Visual Tracking / Lines Observation | 13,4,17,3,27,14,5,9,8 | `N/A` (❌) | `3,3,3,3,3,3,3,3,3` (❌) | `N/A` (❌) | **0.0%** |
| 8323 | Visual Tracking / Lines Observation | 17,3,6,4,6 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8324 | Visual Tracking / Lines Observation | 13,4,9,15,4,4 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8325 | Visual Tracking / Lines Observation | 14,5,9,4,7,10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 431 | Spatial Perception / 3D Views | A | `B` (❌) | `D` (❌) | `B` (❌) | **0.0%** |
| 514 | Spatial Perception / 3D Views | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 524 | Spatial Perception / 3D Views | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 526 | Spatial Perception / 3D Views | 1-B,2-D,3-A,4-C | `1-A, 2-B, 3-C, 4-D` (❌) | `1-D, 2-B, 3-A, 4-C` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 527 | Spatial Perception / 3D Views | E | `D` (❌) | `D` (❌) | `B` (❌) | **0.0%** |
| 548 | Spatial Perception / 3D Views | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 562 | Spatial Perception / 3D Views | A | `B` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 694 | Spatial Perception / 3D Views | D | `C` (❌) | `E` (❌) | `E` (❌) | **0.0%** |
| 696 | Spatial Perception / 3D Views | D | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 713 | Spatial Perception / 3D Views | C | `A` (❌) | `D` (❌) | `N/A` (❌) | **0.0%** |
| 886 | Spatial Perception / 3D Views | C | `B` (❌) | `C` (✅) | `C` (✅) | **66.7%** |
| 888 | Spatial Perception / 3D Views | C | `B` (❌) | `B` (❌) | `C` (✅) | **33.3%** |
| 2004 | Spatial Perception / 3D Views | A | `C` (❌) | `C` (❌) | `B` (❌) | **0.0%** |
| 4047 | Spatial Perception / 3D Views | A-3,B-1,C-4,D-2,F-5,G-6,E-7,H-8 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5285 | Spatial Perception / 3D Views | 1-15,2-12,3-14,4-11,5-9,6-16,7-13,8-10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5340 | Spatial Perception / 3D Views | A | `B` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 5432 | Spatial Perception / 3D Views | C | `B` (❌) | `A` (❌) | `N/A` (❌) | **0.0%** |
| 5694 | Spatial Perception / 3D Views | B | `B` (✅) | `C` (❌) | `B` (✅) | **66.7%** |
| 5695 | Spatial Perception / 3D Views | A | `B` (❌) | `C` (❌) | `A` (✅) | **33.3%** |
| 6038 | Spatial Perception / 3D Views | 1-4,2-10,6-8,7-9,11-5,12-3 | `N/A` (❌) | `1-3,2-3,6-4,7-4,11-3,12-3` (❌) | `N/A` (❌) | **0.0%** |
| 6197 | Spatial Perception / 3D Views | 2-8, 1-3, 5-6, 4-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6220 | Spatial Perception / 3D Views | 1-12,3-2,5-8,7-4,9-6,11-10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6280 | Spatial Perception / 3D Views | 1-C, 2-D, 3-A, 4-B. | `1-A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6340 | Spatial Perception / 3D Views | 1-8,2-9,3-6,10-4,11-7,12-5 | `N/A` (❌) | `N/A` (❌) | `1-4,2-5,3-6,10-7,11-8,12-9` (❌) | **0.0%** |
| 6378 | Spatial Perception / 3D Views | C | `C` (✅) | `A` (❌) | `C` (✅) | **66.7%** |
| 6381 | Spatial Perception / 3D Views | 1-2, 4-7,5-10,8-3,9-6 | `N/A` (❌) | `N/A` (❌) | `1-2, 4-6, 5-10, 8-9, 9-8, 10-5` (❌) | **0.0%** |
| 6434 | Spatial Perception / 3D Views | 1-4,3-2,6-5,8-7 | `1-2,3-4,6-5,8-7` (❌) | `1-2,3-4,6-5,8-7` (❌) | `1-2,3-4,6-5,8-7` (❌) | **0.0%** |
| 799 | Spatial Perception / 3D Cube Unfold | 6,7,9 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1974 | Spatial Perception / 3D Cube Unfold | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 2065 | Spatial Perception / 3D Cube Unfold | The first one in the first row, the third one i... | `N/A` (❌) | `2 \text{nd row}, 1 \text{st column}` (❌) | `N/A` (❌) | **0.0%** |
| 3838 | Spatial Perception / 3D Cube Unfold | 3, 5, 6 | `7` (❌) | `7` (❌) | `N/A` (❌) | **0.0%** |
| 4064 | Spatial Perception / 3D Cube Unfold | E | `C` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4077 | Spatial Perception / 3D Cube Unfold | CD | `D` (❌) | `D` (❌) | `N/A` (❌) | **0.0%** |
| 4759 | Spatial Perception / 3D Cube Unfold | B,C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4760 | Spatial Perception / 3D Cube Unfold | 2,5 | `7` (❌) | `7` (❌) | `N/A` (❌) | **0.0%** |
| 5388 | Spatial Perception / 3D Cube Unfold | 2,3,6 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5449 | Spatial Perception / 3D Cube Unfold | 2,5,7 | `3` (❌) | `N/A` (❌) | `3` (❌) | **0.0%** |
| 6344 | Spatial Perception / 3D Cube Unfold | C | `C` (✅) | `D` (❌) | `D` (❌) | **33.3%** |
| 6467 | Spatial Perception / 3D Cube Unfold | A | `N/A` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 501 | Spatial Perception / Paper Folding | D | `C` (❌) | `D` (✅) | `C` (❌) | **33.3%** |
| 893 | Spatial Perception / Paper Folding | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 1217 | Spatial Perception / Paper Folding | B | `B` (✅) | `C` (❌) | `N/A` (❌) | **33.3%** |
| 3234 | Spatial Perception / Paper Folding | D | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 3240 | Spatial Perception / Paper Folding | F | `C` (❌) | `D` (❌) | `C` (❌) | **0.0%** |
| 4009 | Spatial Perception / Paper Folding | 1, 2, 3, 1 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8333 | Spatial Perception / Paper Folding | 7 | `3` (❌) | `4` (❌) | `3` (❌) | **0.0%** |
| 8334 | Spatial Perception / Paper Folding | 7 | `3` (❌) | `3` (❌) | `3` (❌) | **0.0%** |
| 8335 | Spatial Perception / Paper Folding | 6 | `3` (❌) | `3` (❌) | `3` (❌) | **0.0%** |
| 8336 | Spatial Perception / Paper Folding | 8 | `3` (❌) | `4` (❌) | `3` (❌) | **0.0%** |
| 8337 | Spatial Perception / Paper Folding | 4 | `3` (❌) | `8` (❌) | `4` (✅) | **33.3%** |
| 8338 | Spatial Perception / Paper Folding | 9 | `3` (❌) | `4` (❌) | `3` (❌) | **0.0%** |
| 454 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 480 | Spatial Perception / 3D Pattern Completion | C | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 481 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `B` (❌) | `A` (✅) | **33.3%** |
| 484 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `A` (✅) | `C` (❌) | **33.3%** |
| 502 | Spatial Perception / 3D Pattern Completion | B | `A` (❌) | `B` (✅) | `A` (❌) | **33.3%** |
| 505 | Spatial Perception / 3D Pattern Completion | C | `B` (❌) | `C` (✅) | `A` (❌) | **33.3%** |
| 512 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `B` (❌) | `A` (✅) | **33.3%** |
| 621 | Spatial Perception / 3D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 3777 | Spatial Perception / 3D Pattern Completion | A | `A` (✅) | `C` (❌) | `C` (❌) | **33.3%** |
| 4375 | Spatial Perception / 3D Pattern Completion | B | `B` (✅) | `A` (❌) | `B` (✅) | **66.7%** |
| 4391 | Spatial Perception / 3D Pattern Completion | C | `B` (❌) | `B` (❌) | `A` (❌) | **0.0%** |
| 4420 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4735 | Spatial Perception / 3D Pattern Completion | A | `A` (✅) | `B` (❌) | `B` (❌) | **33.3%** |
| 5308 | Spatial Perception / 3D Pattern Completion | C | `B` (❌) | `C` (✅) | `B` (❌) | **33.3%** |
| 5320 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `A` (✅) | `B` (❌) | **33.3%** |
| 5525 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 5531 | Spatial Perception / 3D Pattern Completion | B | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 6430 | Spatial Perception / 3D Pattern Completion | C | `N/A` (❌) | `A` (❌) | `C` (✅) | **33.3%** |
| 4453 | Spatial Perception / Count 3D blocks | 7 | `6` (❌) | `7` (✅) | `6` (❌) | **33.3%** |
| 4456 | Spatial Perception / Count 3D blocks | 7 | `7` (✅) | `7` (✅) | `7` (✅) | **100.0%** |
| 4457 | Spatial Perception / Count 3D blocks | 8 | `5` (❌) | `7` (❌) | `7` (❌) | **0.0%** |
| 4458 | Spatial Perception / Count 3D blocks | 10 | `10` (✅) | `10` (✅) | `9` (❌) | **66.7%** |
| 4460 | Spatial Perception / Count 3D blocks | 9 | `9` (✅) | `8` (❌) | `9` (✅) | **66.7%** |
| 4593 | Spatial Perception / Count 3D blocks | 9 | `8` (❌) | `7` (❌) | `8` (❌) | **0.0%** |
| 4594 | Spatial Perception / Count 3D blocks | 13 | `10` (❌) | `10` (❌) | `N/A` (❌) | **0.0%** |
| 4596 | Spatial Perception / Count 3D blocks | 13 | `10` (❌) | `10` (❌) | `N/A` (❌) | **0.0%** |
| 4597 | Spatial Perception / Count 3D blocks | 13 | `10` (❌) | `11` (❌) | `10` (❌) | **0.0%** |
| 4598 | Spatial Perception / Count 3D blocks | 16 | `10` (❌) | `10` (❌) | `11` (❌) | **0.0%** |
| 4599 | Spatial Perception / Count 3D blocks | 17 | `14` (❌) | `13` (❌) | `N/A` (❌) | **0.0%** |
| 4603 | Spatial Perception / Count 3D blocks | 17 | `14` (❌) | `11` (❌) | `10` (❌) | **0.0%** |
| 4604 | Spatial Perception / Count 3D blocks | 21 | `13` (❌) | `14` (❌) | `14` (❌) | **0.0%** |
| 4607 | Spatial Perception / Count 3D blocks | 26 | `14` (❌) | `12` (❌) | `12` (❌) | **0.0%** |
| 4610 | Spatial Perception / Count 3D blocks | 13 | `12` (❌) | `10` (❌) | `10` (❌) | **0.0%** |
| 4613 | Spatial Perception / Count 3D blocks | 15 | `13` (❌) | `10` (❌) | `10` (❌) | **0.0%** |
| 4614 | Spatial Perception / Count 3D blocks | 18 | `10` (❌) | `14` (❌) | `15` (❌) | **0.0%** |
| 4616 | Spatial Perception / Count 3D blocks | 23 | `27` (❌) | `27` (❌) | `N/A` (❌) | **0.0%** |
| 4618 | Spatial Perception / Count 3D blocks | 21 | `10` (❌) | `27` (❌) | `N/A` (❌) | **0.0%** |
| 4619 | Spatial Perception / Count 3D blocks | 21 | `20` (❌) | `27` (❌) | `18` (❌) | **0.0%** |
| 4621 | Spatial Perception / Count 3D blocks | 22 | `27` (❌) | `21` (❌) | `N/A` (❌) | **0.0%** |
| 4624 | Spatial Perception / Count 3D blocks | 19 | `14` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 434 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 435 | Visual Pattern Recognition / Overlay Patterns | 2,9 | `N/A` (❌) | `none` (❌) | `2` (❌) | **0.0%** |
| 438 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 441 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 458 | Visual Pattern Recognition / Overlay Patterns | A | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 465 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 479 | Visual Pattern Recognition / Overlay Patterns | A | `N/A` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 504 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 509 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 536 | Visual Pattern Recognition / Overlay Patterns | 3,9 | `N/A` (❌) | `N/A` (❌) | `2,7` (❌) | **0.0%** |
| 625 | Visual Pattern Recognition / Overlay Patterns | C | `C` (✅) | `N/A` (❌) | `C` (✅) | **66.7%** |
| 664 | Visual Pattern Recognition / Overlay Patterns | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 693 | Visual Pattern Recognition / Overlay Patterns | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 708 | Visual Pattern Recognition / Overlay Patterns | A | `N/A` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 3992 | Visual Pattern Recognition / Overlay Patterns | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 3993 | Visual Pattern Recognition / Overlay Patterns | A | `B` (❌) | `C` (❌) | `N/A` (❌) | **0.0%** |
| 4097 | Visual Pattern Recognition / Overlay Patterns | A | `B` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 362 | Visual Pattern Recognition / Logic Patterns | A | `N/A` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 448 | Visual Pattern Recognition / Logic Patterns | B | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 467 | Visual Pattern Recognition / Logic Patterns | F | `(B)` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 487 | Visual Pattern Recognition / Logic Patterns | A | `C` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 553 | Visual Pattern Recognition / Logic Patterns | 1 | `7` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 642 | Visual Pattern Recognition / Logic Patterns | C | `N/A` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 657 | Visual Pattern Recognition / Logic Patterns | F | `N/A` (❌) | `N/A` (❌) | `(F)` (✅) | **33.3%** |
| 669 | Visual Pattern Recognition / Logic Patterns | A | `N/A` (❌) | `F` (❌) | `B` (❌) | **0.0%** |
| 676 | Visual Pattern Recognition / Logic Patterns | B | `D` (❌) | `C` (❌) | `B` (✅) | **33.3%** |
| 687 | Visual Pattern Recognition / Logic Patterns | E | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 718 | Visual Pattern Recognition / Logic Patterns | E | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1293 | Visual Pattern Recognition / Logic Patterns | D | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 1914 | Visual Pattern Recognition / Logic Patterns | 2-9 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1925 | Visual Pattern Recognition / Logic Patterns | 3 and 11 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 510 | Visual Pattern Recognition / Rotation Patterns | 6,4,2 | `1, 2, 3` (❌) | `1, 2, 3` (❌) | `1,2,3` (❌) | **0.0%** |
| 540 | Visual Pattern Recognition / Rotation Patterns | B | `B` (✅) | `B` (✅) | `C` (❌) | **66.7%** |
| 631 | Visual Pattern Recognition / Rotation Patterns | F | `N/A` (❌) | `N/A` (❌) | `E` (❌) | **0.0%** |
| 684 | Visual Pattern Recognition / Rotation Patterns | C | `C` (✅) | `B` (❌) | `C` (✅) | **66.7%** |
| 4180 | Visual Pattern Recognition / Rotation Patterns | C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5293 | Visual Pattern Recognition / Rotation Patterns | B | `N/A` (❌) | `B` (✅) | `D` (❌) | **33.3%** |
| 5519 | Visual Pattern Recognition / Rotation Patterns | C | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 5565 | Visual Pattern Recognition / Rotation Patterns | B | `D` (❌) | `B` (✅) | `D` (❌) | **33.3%** |
| 6455 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 6462 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 537 | Visual Pattern Recognition / Mirroring Patterns | D | `B` (❌) | `D` (✅) | `C` (❌) | **33.3%** |
| 538 | Visual Pattern Recognition / Mirroring Patterns | 1-2,3-6,4-5 | `1-6, 2-5, 3-4` (❌) | `1-6, 2-5, 3-4` (❌) | `1-2, 3-4, 5-6` (❌) | **0.0%** |
| 547 | Visual Pattern Recognition / Mirroring Patterns | 8 | `9` (❌) | `3` (❌) | `9` (❌) | **0.0%** |
| 773 | Visual Pattern Recognition / Mirroring Patterns | 1-4,2-5,3-6 | `1-2, 3-4, 5-6` (❌) | `1-6, 2-5, 3-4` (❌) | `1-6, 2-5, 3-4` (❌) | **0.0%** |
| 819 | Visual Pattern Recognition / Mirroring Patterns | C | `D` (❌) | `B` (❌) | `D` (❌) | **0.0%** |
| 1929 | Visual Pattern Recognition / Mirroring Patterns | 1-7, 2-4, 3-10, 5-11, 6-8, 9-12 | `1-10, 4-8` (❌) | `N/A` (❌) | `1-4` (❌) | **0.0%** |
| 3691 | Visual Pattern Recognition / Mirroring Patterns | C | `C` (✅) | `D` (❌) | `D` (❌) | **33.3%** |
| 4769 | Visual Pattern Recognition / Mirroring Patterns | 1-6, 2-7, 3-4, 5-10, 8-12, 9-11 | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | `1-7,2-8,3-9,4-10,5-11,6-12` (❌) | **0.0%** |
| 4785 | Visual Pattern Recognition / Mirroring Patterns | 1-7, 2-4, 3-5, 6-8 | `1-8, 2-7, 3-6, 4-5` (❌) | `N/A` (❌) | `1-2, 3-4, 5-6, 7-8` (❌) | **0.0%** |
| 5288 | Visual Pattern Recognition / Mirroring Patterns | 1-6,2-11,3-9,4-12,5-7,8-10 | `1-3,4-7,2-5` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |