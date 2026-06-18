# Detailed Evaluation Results: results_local_gemma_4_rl

## 📊 Summary Statistics
```text
Overall Average Accuracy: 0.0954 ± 0.0105

Type-wise Average Accuracy:
  Fine-grained Discrimination: 0.0838 ± 0.0126
  Spatial Perception: 0.1355 ± 0.0226
  Visual Pattern Recognition: 0.0654 ± 0.0333
  Visual Tracking: 0.0924 ± 0.0057

Subtype-wise Average Accuracy:
  1Fine-grained Discrimination/2D Pattern Completion: 0.2833 ± 0.0624
  1Fine-grained Discrimination/Count Clusters: 0.0370 ± 0.0262
  1Fine-grained Discrimination/Count Same Patterns: 0.0286 ± 0.0233
  1Fine-grained Discrimination/Find the different: 0.0000 ± 0.0000
  1Fine-grained Discrimination/Find the same: 0.0392 ± 0.0277
  1Fine-grained Discrimination/Find the shadow: 0.0725 ± 0.0205
  1Fine-grained Discrimination/Pattern and Color Completion: 0.1833 ± 0.0236
  1Fine-grained Discrimination/Reconstruction: 0.0238 ± 0.0337
  2Visual Tracking/Connect the lines: 0.0877 ± 0.0248
  2Visual Tracking/Lines Observation: 0.0000 ± 0.0000
  2Visual Tracking/Maze: 0.1667 ± 0.0236
  2Visual Tracking/Metro map: 0.0278 ± 0.0393
  2Visual Tracking/Recognize numbers and letters: 0.1014 ± 0.0205
  3Spatial Perception/3D Cube Unfold: 0.0000 ± 0.0000
  3Spatial Perception/3D Pattern Completion: 0.2778 ± 0.0454
  3Spatial Perception/3D Views: 0.0988 ± 0.0462
  3Spatial Perception/Count 3D blocks: 0.1061 ± 0.0214
  3Spatial Perception/Paper Folding: 0.1944 ± 0.0393
  4Visual Pattern Recognition/Logic Patterns: 0.0476 ± 0.0673
  4Visual Pattern Recognition/Mirroring Patterns: 0.1000 ± 0.0000
  4Visual Pattern Recognition/Overlay Patterns: 0.0588 ± 0.0480
  4Visual Pattern Recognition/Rotation Patterns: 0.0667 ± 0.0471
```

## 📝 Detailed Task-wise Results
Total evaluated tasks: **388**

| Task ID | Type / Subtype | Ground Truth | Pass 1 Ans (Judge) | Pass 2 Ans (Judge) | Pass 3 Ans (Judge) | Accuracy |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 445 | Fine-grained Discrimination / Find the different | (4,7) | `(2,3)` (❌) | `(3,6)` (❌) | `(1,2)` (❌) | **0.0%** |
| 464 | Fine-grained Discrimination / Find the different | (5,9) | `(1, 10)` (❌) | `N/A` (❌) | `(10, 25)` (❌) | **0.0%** |
| 507 | Fine-grained Discrimination / Find the different | (5,7) | `(4, 7)` (❌) | `(4,7)` (❌) | `(4,8)` (❌) | **0.0%** |
| 525 | Fine-grained Discrimination / Find the different | (7,8) | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 534 | Fine-grained Discrimination / Find the different | (6,12) | `(10, 15)` (❌) | `(8, 10)` (❌) | `(4,18)` (❌) | **0.0%** |
| 638 | Fine-grained Discrimination / Find the different | Row 4 Column 17 | `Row 1 Column 14` (❌) | `Row 7 Column 16` (❌) | `Row 6 Column 13` (❌) | **0.0%** |
| 779 | Fine-grained Discrimination / Find the different | (10, 9) | `(10, 3)` (❌) | `(4, 10)` (❌) | `(8, 10)` (❌) | **0.0%** |
| 879 | Fine-grained Discrimination / Find the different | 10,5 | `(13,7)` (❌) | `N/A` (❌) | `(7,7)` (❌) | **0.0%** |
| 910 | Fine-grained Discrimination / Find the different | 9,5 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 984 | Fine-grained Discrimination / Find the different | (6,10) | `(5,11)` (❌) | `(5,11)` (❌) | `(5,10)` (❌) | **0.0%** |
| 986 | Fine-grained Discrimination / Find the different | (11,4) | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 988 | Fine-grained Discrimination / Find the different | (9,7) | `(11,10)` (❌) | `(11,10)` (❌) | `(20,10)` (❌) | **0.0%** |
| 4152 | Fine-grained Discrimination / Find the different | (7,2) | `N/A` (❌) | `(2,6)` (❌) | `(4,1)` (❌) | **0.0%** |
| 6161 | Fine-grained Discrimination / Find the different | (7,8) | `(4,10)` (❌) | `(7,3)` (❌) | `(4, 4)` (❌) | **0.0%** |
| 6164 | Fine-grained Discrimination / Find the different | (9,2) | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6165 | Fine-grained Discrimination / Find the different | 6-7 | `N/A` (❌) | `N/A` (❌) | `No different silhouette found` (❌) | **0.0%** |
| 437 | Fine-grained Discrimination / Find the same | 1-7,2-9,3-10,4-8,6-11 | `No identical pairs` (❌) | `No identical pairs` (❌) | `N/A` (❌) | **0.0%** |
| 462 | Fine-grained Discrimination / Find the same | D | `A` (❌) | `A` (❌) | `B` (❌) | **0.0%** |
| 469 | Fine-grained Discrimination / Find the same | 2-7 | `1-4` (❌) | `1-4` (❌) | `2-3` (❌) | **0.0%** |
| 475 | Fine-grained Discrimination / Find the same | (1,3)-(3,1) | `(1,1)-(2,3)` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 476 | Fine-grained Discrimination / Find the same | 4-11 | `1-3` (❌) | `1-3` (❌) | `1-3` (❌) | **0.0%** |
| 478 | Fine-grained Discrimination / Find the same | 2,3,6,7,10 | `2,3,4,5,6,7,8,9,10` (❌) | `2,3,4,5,6,7,8,9,10` (❌) | `2,3,4,5,6,7,8,9,10` (❌) | **0.0%** |
| 498 | Fine-grained Discrimination / Find the same | BG,CE,DF | `N/A` (❌) | `N/A` (❌) | `AB,DE,FG` (❌) | **0.0%** |
| 522 | Fine-grained Discrimination / Find the same | E | `D` (❌) | `E` (✅) | `A` (❌) | **33.3%** |
| 617 | Fine-grained Discrimination / Find the same | C | `A` (❌) | `B` (❌) | `A` (❌) | **0.0%** |
| 626 | Fine-grained Discrimination / Find the same | Second row third column | `N/A` (❌) | `N/A` (❌) | `Row 2, Column 3` (✅) | **33.3%** |
| 635 | Fine-grained Discrimination / Find the same | 9-12 | `N/A` (❌) | `No pairs` (❌) | `1-2` (❌) | **0.0%** |
| 651 | Fine-grained Discrimination / Find the same | 4-11 | `2-9` (❌) | `10-12` (❌) | `1-2` (❌) | **0.0%** |
| 711 | Fine-grained Discrimination / Find the same | (2-1)-(3-3) | `(1-1)-(2-1)` (❌) | `(1-2)-(2-1)` (❌) | `(1-1)-(2-1)` (❌) | **0.0%** |
| 720 | Fine-grained Discrimination / Find the same | 12 | `1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19...` (❌) | `N/A` (❌) | `1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19...` (❌) | **0.0%** |
| 4698 | Fine-grained Discrimination / Find the same | 2D,6A,4B,1B,5C,1F | `N/A` (❌) | `1A, 2B, 3C, 4D, 5E, 6F` (❌) | `N/A` (❌) | **0.0%** |
| 5597 | Fine-grained Discrimination / Find the same | 2,4,5,6,7,9 | `2,3,4,5,6,7,8,9,10` (❌) | `3,4,6,7,9,10` (❌) | `N/A` (❌) | **0.0%** |
| 7568 | Fine-grained Discrimination / Find the same | F | `A` (❌) | `(B)` (❌) | `B` (❌) | **0.0%** |
| 459 | Fine-grained Discrimination / Find the shadow | 1-4,3-12,5-10,7-2,9-6,11-8 | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | `1-10,3-4,5-6,7-8,9-12,11-2` (❌) | `1-2,3-4,5-6,7-8,9-10,11-12` (❌) | **0.0%** |
| 644 | Fine-grained Discrimination / Find the shadow | 1-6,2-5,3-8,4-11,5-12,6-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 826 | Fine-grained Discrimination / Find the shadow | 1-6,3-4,5-8,7-12,9-10,11-2 | `1-2, 3-4` (❌) | `N/A` (❌) | `1-4,3-6,5-12,7-8,9-10,11-2` (❌) | **0.0%** |
| 4994 | Fine-grained Discrimination / Find the shadow | D | `B` (❌) | `C` (❌) | `B` (❌) | **0.0%** |
| 4996 | Fine-grained Discrimination / Find the shadow | C | `N/A` (❌) | `None` (❌) | `None` (❌) | **0.0%** |
| 4998 | Fine-grained Discrimination / Find the shadow | B | `C` (❌) | `C` (❌) | `None of the above` (❌) | **0.0%** |
| 5001 | Fine-grained Discrimination / Find the shadow | Second row third column | `2, 2` (❌) | `1, 2` (❌) | `2, 2` (❌) | **0.0%** |
| 5004 | Fine-grained Discrimination / Find the shadow | Second row first column | `1, 2` (❌) | `1, 2` (❌) | `1, 1` (✅) | **33.3%** |
| 5006 | Fine-grained Discrimination / Find the shadow | Row 1, Column 2 | `Row 2, Column 2` (❌) | `Middle row, left column` (❌) | `Second\ row, second\ column` (✅) | **33.3%** |
| 5008 | Fine-grained Discrimination / Find the shadow | The second row, third column | `2, 1` (❌) | `2, 3` (✅) | `2, 2` (❌) | **33.3%** |
| 5009 | Fine-grained Discrimination / Find the shadow | Row 1 Column 3 | `N/A` (❌) | `2, 3` (✅) | `2, 2` (❌) | **33.3%** |
| 5011 | Fine-grained Discrimination / Find the shadow | Third row first column | `Row 2, Column 2` (❌) | `Row 2, Column 3` (❌) | `Row 2, Column 3` (❌) | **0.0%** |
| 5013 | Fine-grained Discrimination / Find the shadow | Third Row Second Column | `(2, 2)` (❌) | `2, 2` (❌) | `2, 2` (❌) | **0.0%** |
| 5016 | Fine-grained Discrimination / Find the shadow | 1-C,2-G,3-D,4-E,5-B,6-F,7-A | `N/A` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D, 5-E, 6-F, 7-G` (❌) | **0.0%** |
| 5018 | Fine-grained Discrimination / Find the shadow | The third row and first column | `Row 1, Column 1` (❌) | `Row 1, Column 1` (❌) | `Row 4, Column 1` (❌) | **0.0%** |
| 5020 | Fine-grained Discrimination / Find the shadow | Second column, first one | `3, 3` (❌) | `3, 1` (❌) | `3, 3` (❌) | **0.0%** |
| 5022 | Fine-grained Discrimination / Find the shadow | The first row and second column | `Bottom row, left column` (❌) | `3, 3` (❌) | `3, 1` (❌) | **0.0%** |
| 5023 | Fine-grained Discrimination / Find the shadow | Second row second | `4, 3` (❌) | `1, 3` (❌) | `4, 2` (❌) | **0.0%** |
| 5025 | Fine-grained Discrimination / Find the shadow | 1-G,2-D,3-A,4-F,6-B,7-E,8-H,9-C | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D, 9-E, 6-F, 7-G, 8-H` (❌) | `N/A` (❌) | **0.0%** |
| 5026 | Fine-grained Discrimination / Find the shadow | 1-F,2-D,3-E,4-B,6-H,7-A,8-G,9-C | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D, 6-E, 7-F, 8-G, 9-H` (❌) | `N/A` (❌) | **0.0%** |
| 5030 | Fine-grained Discrimination / Find the shadow | 1-F,2-G,3-D,4-B,6-C,7-H,8-A,9-E | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6504 | Fine-grained Discrimination / Find the shadow | 1-4,2-3,3-1,4-2 | `1-4, 2-3, 3-1, 4-2` (✅) | `1-1, 2-4, 3-3, 4-2` (❌) | `1-4, 2-3, 3-2, 4-1` (❌) | **33.3%** |
| 6512 | Fine-grained Discrimination / Find the shadow | 1-7,2-8,3-6,4-10,5-9 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 535 | Fine-grained Discrimination / Reconstruction | B | `C` (❌) | `C` (❌) | `A` (❌) | **0.0%** |
| 2353 | Fine-grained Discrimination / Reconstruction | C | `A` (❌) | `C` (✅) | `A` (❌) | **33.3%** |
| 5270 | Fine-grained Discrimination / Reconstruction | 2,3,5 | `1, 3, 5` (❌) | `1, 2, 3, 5` (❌) | `1, 2, 3, 4, 5` (❌) | **0.0%** |
| 5271 | Fine-grained Discrimination / Reconstruction | 1,3,4 | `1, 2, 3, 4` (❌) | `1,2,3,4,5` (❌) | `1, 2, 3, 4` (❌) | **0.0%** |
| 5274 | Fine-grained Discrimination / Reconstruction | 1,3,4,5 | `1, 2, 3, 4` (❌) | `1,3` (❌) | `1,2,3,4` (❌) | **0.0%** |
| 5275 | Fine-grained Discrimination / Reconstruction | 2,3,4,5 | `1, 2, 5` (❌) | `N/A` (❌) | `1, 2, 3, 4, 5` (❌) | **0.0%** |
| 5276 | Fine-grained Discrimination / Reconstruction | 1,3,4,6,8 | `1, 2, 3, 4` (❌) | `N/A` (❌) | `1, 3, 4, 7` (❌) | **0.0%** |
| 5277 | Fine-grained Discrimination / Reconstruction | 1,2,4,5,8 | `1, 4, 6` (❌) | `N/A` (❌) | `1, 3, 4, 5, 8` (❌) | **0.0%** |
| 5339 | Fine-grained Discrimination / Reconstruction | 1-9, 2-8, 3-10, 4-6, 5-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6131 | Fine-grained Discrimination / Reconstruction | 1-B,2-C,3-D,4-A | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6134 | Fine-grained Discrimination / Reconstruction | 1-B,2-D,3-A,4-C | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `N/A` (❌) | **0.0%** |
| 6136 | Fine-grained Discrimination / Reconstruction | 1-C,2-D,3-A,4-B | `1-A, 2-B, 3-C, 4-D` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6137 | Fine-grained Discrimination / Reconstruction | 1-D,2-A,3-B,4-C | `1-A, 2-B, 3-C, 4-D` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 6273 | Fine-grained Discrimination / Reconstruction | A-6, B-3, C-4, D-1, E-2, F-5 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 457 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 494 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 637 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 640 | Fine-grained Discrimination / 2D Pattern Completion | A | `C` (❌) | `B` (❌) | `Choices: (A)` (✅) | **33.3%** |
| 673 | Fine-grained Discrimination / 2D Pattern Completion | A | `C` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 765 | Fine-grained Discrimination / 2D Pattern Completion | A | `C` (❌) | `B` (❌) | `A` (✅) | **33.3%** |
| 876 | Fine-grained Discrimination / 2D Pattern Completion | B | `C` (❌) | `B` (✅) | `C` (❌) | **33.3%** |
| 3995 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4026 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `N/A` (❌) | **66.7%** |
| 4104 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 4133 | Fine-grained Discrimination / 2D Pattern Completion | A | `D` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 4142 | Fine-grained Discrimination / 2D Pattern Completion | C | `D` (❌) | `B` (❌) | `C` (✅) | **33.3%** |
| 4173 | Fine-grained Discrimination / 2D Pattern Completion | C | `C` (✅) | `N/A` (❌) | `N/A` (❌) | **33.3%** |
| 4188 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 4190 | Fine-grained Discrimination / 2D Pattern Completion | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 4386 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 4399 | Fine-grained Discrimination / 2D Pattern Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 4405 | Fine-grained Discrimination / 2D Pattern Completion | D | `B` (❌) | `A` (❌) | `B` (❌) | **0.0%** |
| 4415 | Fine-grained Discrimination / 2D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 4712 | Fine-grained Discrimination / 2D Pattern Completion | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 559 | Fine-grained Discrimination / Pattern and Color Completion | A | `C` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 628 | Fine-grained Discrimination / Pattern and Color Completion | C | `N/A` (❌) | `C` (✅) | `B` (❌) | **33.3%** |
| 633 | Fine-grained Discrimination / Pattern and Color Completion | B | `Answer: (B)` (✅) | `B` (✅) | `B` (✅) | **100.0%** |
| 639 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 645 | Fine-grained Discrimination / Pattern and Color Completion | A | `A` (✅) | `A` (✅) | `A` (✅) | **100.0%** |
| 652 | Fine-grained Discrimination / Pattern and Color Completion | C | `C` (✅) | `C` (✅) | `B` (❌) | **66.7%** |
| 695 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 699 | Fine-grained Discrimination / Pattern and Color Completion | D | `B` (❌) | `C` (❌) | `A` (❌) | **0.0%** |
| 721 | Fine-grained Discrimination / Pattern and Color Completion | A | `C` (❌) | `C` (❌) | `A` (✅) | **33.3%** |
| 790 | Fine-grained Discrimination / Pattern and Color Completion | D | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 792 | Fine-grained Discrimination / Pattern and Color Completion | C | `N/A` (❌) | `A` (❌) | `N/A` (❌) | **0.0%** |
| 1594 | Fine-grained Discrimination / Pattern and Color Completion | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 4146 | Fine-grained Discrimination / Pattern and Color Completion | C | `A` (❌) | `B` (❌) | `A` (❌) | **0.0%** |
| 4148 | Fine-grained Discrimination / Pattern and Color Completion | C | `B` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 4181 | Fine-grained Discrimination / Pattern and Color Completion | B | `C` (❌) | `D` (❌) | `C` (❌) | **0.0%** |
| 4768 | Fine-grained Discrimination / Pattern and Color Completion | 1-D,2-B,3-A,4-C | `N/A` (❌) | `N/A` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 5123 | Fine-grained Discrimination / Pattern and Color Completion | Row 2, Column 3 | `1, 3` (❌) | `N/A` (❌) | `2, 2` (❌) | **0.0%** |
| 5399 | Fine-grained Discrimination / Pattern and Color Completion | B | `C` (❌) | `C` (❌) | `B` (✅) | **33.3%** |
| 6206 | Fine-grained Discrimination / Pattern and Color Completion | 2,6,8 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 7858 | Fine-grained Discrimination / Pattern and Color Completion | B | `N/A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 4534 | Fine-grained Discrimination / Count Same Patterns | 14 | `13` (❌) | `10` (❌) | `14` (✅) | **33.3%** |
| 4536 | Fine-grained Discrimination / Count Same Patterns | 15 | `9` (❌) | `10` (❌) | `10` (❌) | **0.0%** |
| 4537 | Fine-grained Discrimination / Count Same Patterns | 13 | `7` (❌) | `10` (❌) | `9` (❌) | **0.0%** |
| 4540 | Fine-grained Discrimination / Count Same Patterns | 18 | `13` (❌) | `11` (❌) | `13` (❌) | **0.0%** |
| 4552 | Fine-grained Discrimination / Count Same Patterns | 54 | `33` (❌) | `26` (❌) | `28` (❌) | **0.0%** |
| 4553 | Fine-grained Discrimination / Count Same Patterns | 58 | `44` (❌) | `45` (❌) | `34` (❌) | **0.0%** |
| 4554 | Fine-grained Discrimination / Count Same Patterns | 42 | `21` (❌) | `19` (❌) | `20` (❌) | **0.0%** |
| 4556 | Fine-grained Discrimination / Count Same Patterns | 67 | `49` (❌) | `46` (❌) | `43` (❌) | **0.0%** |
| 4558 | Fine-grained Discrimination / Count Same Patterns | 54 | `53` (❌) | `37` (❌) | `43` (❌) | **0.0%** |
| 4560 | Fine-grained Discrimination / Count Same Patterns | 36 | `15` (❌) | `13` (❌) | `20` (❌) | **0.0%** |
| 4561 | Fine-grained Discrimination / Count Same Patterns | 38 | `22` (❌) | `22` (❌) | `21` (❌) | **0.0%** |
| 4562 | Fine-grained Discrimination / Count Same Patterns | 36 | `16` (❌) | `16` (❌) | `16` (❌) | **0.0%** |
| 4564 | Fine-grained Discrimination / Count Same Patterns | 32 | `18` (❌) | `17` (❌) | `17` (❌) | **0.0%** |
| 4566 | Fine-grained Discrimination / Count Same Patterns | 17 | `8` (❌) | `8` (❌) | `8` (❌) | **0.0%** |
| 4568 | Fine-grained Discrimination / Count Same Patterns | 34 | `22` (❌) | `15` (❌) | `17` (❌) | **0.0%** |
| 4571 | Fine-grained Discrimination / Count Same Patterns | 36 | `26` (❌) | `21` (❌) | `21` (❌) | **0.0%** |
| 5073 | Fine-grained Discrimination / Count Same Patterns | 23 | `19` (❌) | `0` (❌) | `N/A` (❌) | **0.0%** |
| 5074 | Fine-grained Discrimination / Count Same Patterns | 22 | `12` (❌) | `9` (❌) | `16` (❌) | **0.0%** |
| 5081 | Fine-grained Discrimination / Count Same Patterns | 18 | `12` (❌) | `12` (❌) | `12` (❌) | **0.0%** |
| 5082 | Fine-grained Discrimination / Count Same Patterns | 14 | `16` (❌) | `12` (❌) | `13` (❌) | **0.0%** |
| 5083 | Fine-grained Discrimination / Count Same Patterns | 24 | `16` (❌) | `12` (❌) | `16` (❌) | **0.0%** |
| 5084 | Fine-grained Discrimination / Count Same Patterns | 24 | `12` (❌) | `12` (❌) | `12` (❌) | **0.0%** |
| 5085 | Fine-grained Discrimination / Count Same Patterns | 18 | `9` (❌) | `16` (❌) | `26` (❌) | **0.0%** |
| 5086 | Fine-grained Discrimination / Count Same Patterns | 34 | `8` (❌) | `10` (❌) | `6` (❌) | **0.0%** |
| 5357 | Fine-grained Discrimination / Count Same Patterns | 8, 3, 7, 4, 5, 6 | `7,0,8,7,4,0` (❌) | `N/A` (❌) | `9,0,9,8,7,4` (❌) | **0.0%** |
| 5358 | Fine-grained Discrimination / Count Same Patterns | 7, 4, 5, 9, 2 | `N/A` (❌) | `6,5,3,2,0` (❌) | `N/A` (❌) | **0.0%** |
| 5638 | Fine-grained Discrimination / Count Same Patterns | 4 | `1` (❌) | `0` (❌) | `0` (❌) | **0.0%** |
| 5639 | Fine-grained Discrimination / Count Same Patterns | 4 | `1` (❌) | `0` (❌) | `1` (❌) | **0.0%** |
| 5640 | Fine-grained Discrimination / Count Same Patterns | 5 | `5` (✅) | `8` (❌) | `0` (❌) | **33.3%** |
| 5781 | Fine-grained Discrimination / Count Same Patterns | 5 | `32` (❌) | `10` (❌) | `27` (❌) | **0.0%** |
| 5786 | Fine-grained Discrimination / Count Same Patterns | 10 | `10` (✅) | `0` (❌) | `0` (❌) | **33.3%** |
| 6421 | Fine-grained Discrimination / Count Same Patterns | 7,6,2,7,9,5 | `N/A` (❌) | `N/A` (❌) | `5,6,4,5,4,2` (❌) | **0.0%** |
| 6436 | Fine-grained Discrimination / Count Same Patterns | 8,7,3,2 | `4,4,4,4` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6466 | Fine-grained Discrimination / Count Same Patterns | 5,6,5,8 | `5,5,5,5` (❌) | `3,4,4,4` (❌) | `N/A` (❌) | **0.0%** |
| 6475 | Fine-grained Discrimination / Count Same Patterns | 15,10,11,15 | `8,4,8,6` (❌) | `7,8,7,8` (❌) | `15,4,10,9` (❌) | **0.0%** |
| 496 | Fine-grained Discrimination / Count Clusters | 18 | `0` (❌) | `9` (❌) | `9` (❌) | **0.0%** |
| 4650 | Fine-grained Discrimination / Count Clusters | 19 | `22` (❌) | `22` (❌) | `19` (✅) | **33.3%** |
| 4652 | Fine-grained Discrimination / Count Clusters | 21 | `15` (❌) | `18` (❌) | `18` (❌) | **0.0%** |
| 4653 | Fine-grained Discrimination / Count Clusters | 9 | `6` (❌) | `7` (❌) | `5` (❌) | **0.0%** |
| 5107 | Fine-grained Discrimination / Count Clusters | 8 | `15` (❌) | `15` (❌) | `10` (❌) | **0.0%** |
| 5113 | Fine-grained Discrimination / Count Clusters | 10 | `12` (❌) | `11` (❌) | `11` (❌) | **0.0%** |
| 5114 | Fine-grained Discrimination / Count Clusters | 9 | `12` (❌) | `10` (❌) | `12` (❌) | **0.0%** |
| 5117 | Fine-grained Discrimination / Count Clusters | 8,7 | `13, 4` (❌) | `13` (❌) | `10,5` (❌) | **0.0%** |
| 5119 | Fine-grained Discrimination / Count Clusters | 10 | `10` (✅) | `11` (❌) | `11` (❌) | **33.3%** |
| 5378 | Fine-grained Discrimination / Count Clusters | 6,3,5,5 | `3,3,4,4` (❌) | `N/A` (❌) | `1,1,1,1` (❌) | **0.0%** |
| 5455 | Fine-grained Discrimination / Count Clusters | 2+6+1+3=12 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5490 | Fine-grained Discrimination / Count Clusters | 8−5=3 | `5-3=2` (❌) | `7-5=2` (❌) | `6-4=2` (❌) | **0.0%** |
| 5492 | Fine-grained Discrimination / Count Clusters | 7−1=6 | `6-1=5` (❌) | `6-1=5` (❌) | `N/A` (❌) | **0.0%** |
| 5795 | Fine-grained Discrimination / Count Clusters | 10,14,12 | `N/A` (❌) | `25` (❌) | `30` (❌) | **0.0%** |
| 6534 | Fine-grained Discrimination / Count Clusters | 1-2, 2-1, 3-4, 4-3 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6555 | Fine-grained Discrimination / Count Clusters | > | `=` (❌) | `=` (❌) | `=` (❌) | **0.0%** |
| 6556 | Fine-grained Discrimination / Count Clusters | < | `>` (❌) | `=` (❌) | `>` (❌) | **0.0%** |
| 6557 | Fine-grained Discrimination / Count Clusters | = | `>` (❌) | `<` (❌) | `<` (❌) | **0.0%** |
| 666 | Visual Tracking / Maze | B | `(B)` (✅) | `(B)` (✅) | `Answer: (B)` (✅) | **100.0%** |
| 674 | Visual Tracking / Maze | E | `N/A` (❌) | `N/A` (❌) | ` (A)` (❌) | **0.0%** |
| 817 | Visual Tracking / Maze | A | `C` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 980 | Visual Tracking / Maze | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 982 | Visual Tracking / Maze | A | `Choice (A)` (✅) | `A` (✅) | `Answer: (B)` (❌) | **66.7%** |
| 983 | Visual Tracking / Maze | A | `Answer: (B)` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 1306 | Visual Tracking / Maze | B | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 1651 | Visual Tracking / Maze | B | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 3782 | Visual Tracking / Maze | C | `B` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5124 | Visual Tracking / Maze | 39 | `37` (❌) | `28` (❌) | `N/A` (❌) | **0.0%** |
| 5127 | Visual Tracking / Maze | 59 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5128 | Visual Tracking / Maze | 50 | `8` (❌) | `N/A` (❌) | `14` (❌) | **0.0%** |
| 5130 | Visual Tracking / Maze | 57 | `N/A` (❌) | `10` (❌) | `N/A` (❌) | **0.0%** |
| 5131 | Visual Tracking / Maze | 53 | `N/A` (❌) | `17` (❌) | `N/A` (❌) | **0.0%** |
| 5133 | Visual Tracking / Maze | 51 | `N/A` (❌) | `12` (❌) | `17` (❌) | **0.0%** |
| 5136 | Visual Tracking / Maze | 27 | `N/A` (❌) | `N/A` (❌) | `23` (❌) | **0.0%** |
| 5139 | Visual Tracking / Maze | 38 | `N/A` (❌) | `11` (❌) | `8` (❌) | **0.0%** |
| 5140 | Visual Tracking / Maze | 52 | `N/A` (❌) | `N/A` (❌) | `10` (❌) | **0.0%** |
| 5142 | Visual Tracking / Maze | 52 | `17` (❌) | `N/A` (❌) | `19` (❌) | **0.0%** |
| 5143 | Visual Tracking / Maze | 55 | `24` (❌) | `18` (❌) | `N/A` (❌) | **0.0%** |
| 770 | Visual Tracking / Connect the lines | A-2,B-3,C-1 | `A-1, B-2, C-3` (❌) | `A-2, B-1, C-3` (❌) | `N/A` (❌) | **0.0%** |
| 1662 | Visual Tracking / Connect the lines | 4,2,6,5,7,3,1 | `N/A` (❌) | `7, 3, 5, 2, 3, 1, 6` (❌) | `N/A` (❌) | **0.0%** |
| 2492 | Visual Tracking / Connect the lines | D | `A` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 4327 | Visual Tracking / Connect the lines | 1-B,2-A,3-C | `1-A, 2-B, 3-C` (❌) | `1-A, 2-B, 3-C` (❌) | `1-A, 2-B, 3-C` (❌) | **0.0%** |
| 4329 | Visual Tracking / Connect the lines | 10,7,7 | `10, 12, 6` (❌) | `N/A` (❌) | `6, 12, 16` (❌) | **0.0%** |
| 4330 | Visual Tracking / Connect the lines | A - Blue, B - Yellow, C - Green | `A-blue, B-yellow, C-green` (✅) | `A-yellow, B-blue, C-green` (❌) | `A-yellow, B-blue, C-green` (❌) | **33.3%** |
| 4332 | Visual Tracking / Connect the lines | 3-Gem,1-Fan,2-Crab,4-Skull | `a-gem,b-fan,c-crab,d-skull` (❌) | `a-gem,b-fan,c-crab,d-skull` (❌) | `a-gem,b-fan,c-crab,d-skull` (❌) | **0.0%** |
| 4337 | Visual Tracking / Connect the lines | 1-Skull #3, 2-Skull #2, 3-Diamond, 4-Skull #1 | `1: Skull \#1, 2: Diamond, 3: Skull \#2, 4: Skul...` (❌) | `Line 1 $\to$ Skull #1, Line 2 $\to$ Diamond, Li...` (❌) | `Line 1 $\to$ Skull #1, Line 2 $\to$ Diamond, Li...` (❌) | **0.0%** |
| 4352 | Visual Tracking / Connect the lines | A-Circle, B-Triangle, C-Rectangle, D-Square, E-... | `A-square, B-circle, C-star, D-triangle, E-recta...` (❌) | `Red-square, Blue-circle, Yellow-pentagram, Gree...` (❌) | `Red-square, Blue-circle, Yellow-pentagram, Gree...` (✅) | **33.3%** |
| 5152 | Visual Tracking / Connect the lines | 1-S,2-N,3-O,4-W,5-M,6-A,7-N | `1-W,2-N,3-N,4-O,5-A,6-M,7-S` (❌) | `1-W,2-N,3-N,4-O,5-A,6-M,7-S` (❌) | `1-W,2-N,3-N,4-O,5-A,6-M,7-S` (❌) | **0.0%** |
| 5154 | Visual Tracking / Connect the lines | A-X,B-Y,C-Z,D-W | `A-W, B-X, C-Y, D-Z` (✅) | `A-W, B-X, C-Y, D-Z` (✅) | `A-W, B-X, C-Y, D-Z` (✅) | **100.0%** |
| 5156 | Visual Tracking / Connect the lines | 1-D,2-I,3-A,4-M,5-O,6-N,7-D | `1-A,2-N,3-D,4-D,5-O,6-I,7-M` (❌) | `1-A,2-N,3-D,4-D,5-O,6-I,7-M` (❌) | `1-A, 2-N, 3-D, 4-D, 5-O, 6-I, 7-M` (❌) | **0.0%** |
| 5161 | Visual Tracking / Connect the lines | 1-U,2-M,3-B,4-R,5-E,6-L,7-L,8-A | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | `1-B,2-L,3-R,4-U,5-A,6-L,7-E,8-M` (❌) | **0.0%** |
| 5164 | Visual Tracking / Connect the lines | 1-H,2-E,3-D,4-G,5-E,6-H,7-O,8-G | `1-E,2-H,3-O,4-E,5-G,6-G,7-H,8-D` (❌) | `N/A` (❌) | `1-E,2-H,3-O,4-E,5-G,6-G,7-H,8-D` (❌) | **0.0%** |
| 5245 | Visual Tracking / Connect the lines | Still,waters,run,deep | `N/A` (❌) | `star, sure, sent, side` (❌) | `N/A` (❌) | **0.0%** |
| 5246 | Visual Tracking / Connect the lines | Better,late,than,never | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5247 | Visual Tracking / Connect the lines | Which,witch,is,which | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5248 | Visual Tracking / Connect the lines | Rolling,red,wagons | `N/A` (❌) | `ring, log, road` (❌) | `RING, GOLD, SON` (❌) | **0.0%** |
| 5249 | Visual Tracking / Connect the lines | Daddy,draws,doors | `N/A` (❌) | `docs, dos, day` (❌) | `N/A` (❌) | **0.0%** |
| 447 | Visual Tracking / Recognize numbers and letters | 2,N,Z,S | `A,S,Z,S` (❌) | `A,S,Z,S` (❌) | `Y,G,B,R` (❌) | **0.0%** |
| 520 | Visual Tracking / Recognize numbers and letters | G,4,D,6 | `4, 4, D, 6` (❌) | `4, 4, D, 6` (❌) | `4,4,D,6` (❌) | **0.0%** |
| 542 | Visual Tracking / Recognize numbers and letters | 6,9,8 | `1, 1, 1` (❌) | `No numbers are present in the image.` (❌) | `No numbers are present in the image.` (❌) | **0.0%** |
| 543 | Visual Tracking / Recognize numbers and letters | 0,9,3 | `Cannot be determined from the image` (❌) | `Not present` (❌) | `No numbers found` (❌) | **0.0%** |
| 544 | Visual Tracking / Recognize numbers and letters | 3,6,2 | `1, 2, 3` (❌) | `N/A` (❌) | `No numbers found` (❌) | **0.0%** |
| 545 | Visual Tracking / Recognize numbers and letters | 3,7,2 | `3, 3, 3` (❌) | `3, 2, 3` (❌) | `3, 3, 3` (❌) | **0.0%** |
| 665 | Visual Tracking / Recognize numbers and letters | D, 2, 4 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 671 | Visual Tracking / Recognize numbers and letters | C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 757 | Visual Tracking / Recognize numbers and letters | AN APPLE | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1298 | Visual Tracking / Recognize numbers and letters | J, U, 3 | `N/A` (❌) | `W, U, 3` (❌) | `W, U, 3` (❌) | **0.0%** |
| 1587 | Visual Tracking / Recognize numbers and letters | D,8,P,T | `O,S,B,A` (❌) | `O, S, B, X` (❌) | `D,8,B,T` (❌) | **0.0%** |
| 5227 | Visual Tracking / Recognize numbers and letters | 3,4,9 | `1, 2, 3` (❌) | `1, 2, 3` (❌) | `1, 2, 3` (❌) | **0.0%** |
| 5228 | Visual Tracking / Recognize numbers and letters | 3,4,5 | `3,4,5` (✅) | `3, 4, 5` (✅) | `2, 3, 4` (❌) | **66.7%** |
| 5229 | Visual Tracking / Recognize numbers and letters | 1,6,7 | `1, 6, 9` (❌) | `N/A` (❌) | `1, 6, 9` (❌) | **0.0%** |
| 5238 | Visual Tracking / Recognize numbers and letters | 3,4,9 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5239 | Visual Tracking / Recognize numbers and letters | 1,4,7 | `No numbers` (❌) | `No numbers present` (❌) | `No numbers are present` (❌) | **0.0%** |
| 5240 | Visual Tracking / Recognize numbers and letters | 2,5,8 | `No numbers` (❌) | `None` (❌) | `None` (❌) | **0.0%** |
| 5241 | Visual Tracking / Recognize numbers and letters | 2,5,9 | `1, 2, 9` (❌) | `2, 5, 9` (✅) | `2, 5, 9` (✅) | **66.7%** |
| 5242 | Visual Tracking / Recognize numbers and letters | 1,3,7 | `1, 3, 7` (✅) | `1, 3, 7` (✅) | `1, 3, 7` (✅) | **100.0%** |
| 5505 | Visual Tracking / Recognize numbers and letters | 2, 7, 5, 9 | `blue,green,red,yellow` (❌) | `Character\_blue,Character\_green,Character\_red...` (❌) | `b,g,r,y` (❌) | **0.0%** |
| 5507 | Visual Tracking / Recognize numbers and letters | O, 8, N, Z | `8, 8, Z, N` (❌) | `8, Z, N` (❌) | `N/A` (❌) | **0.0%** |
| 6435 | Visual Tracking / Recognize numbers and letters | 3,6,1 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6509 | Visual Tracking / Recognize numbers and letters | 4, 6, 5, 5 | `1, 2, 3, 4` (❌) | `N/A` (❌) | `Cannot be determined` (❌) | **0.0%** |
| 8326 | Visual Tracking / Metro map | 6 | `N/A` (❌) | `3` (❌) | `6` (✅) | **33.3%** |
| 8327 | Visual Tracking / Metro map | 8 | `5` (❌) | `7` (❌) | `N/A` (❌) | **0.0%** |
| 8328 | Visual Tracking / Metro map | 11 | `6` (❌) | `9` (❌) | `N/A` (❌) | **0.0%** |
| 8329 | Visual Tracking / Metro map | 4 | `3` (❌) | `N/A` (❌) | `3` (❌) | **0.0%** |
| 8330 | Visual Tracking / Metro map | 8 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8331 | Visual Tracking / Metro map | 10 | `1` (❌) | `1` (❌) | `1` (❌) | **0.0%** |
| 8332 | Visual Tracking / Metro map | 9 | `2` (❌) | `N/A` (❌) | `0` (❌) | **0.0%** |
| 8339 | Visual Tracking / Metro map | 22 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8340 | Visual Tracking / Metro map | 8 | `0` (❌) | `0` (❌) | `N/A` (❌) | **0.0%** |
| 8341 | Visual Tracking / Metro map | 20 | `2` (❌) | `N/A` (❌) | `3` (❌) | **0.0%** |
| 8342 | Visual Tracking / Metro map | 12 | `N/A` (❌) | `N/A` (❌) | `1` (❌) | **0.0%** |
| 8343 | Visual Tracking / Metro map | 11 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8162 | Visual Tracking / Lines Observation | 15,13,12,10,9,9,9,8,8,7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8163 | Visual Tracking / Lines Observation | 17,16,12,12,11,11,9,5,4,3 | `17,14,13,11,9,9,7` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8164 | Visual Tracking / Lines Observation | 14,11,10,9,7,6,4,3 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8165 | Visual Tracking / Lines Observation | 25,7,7,6,6,5,4,4 | `N/A` (❌) | `N/A` (❌) | `8,7,5,4,3,3` (❌) | **0.0%** |
| 8166 | Visual Tracking / Lines Observation | 13,11,10,9,7,6,5,3 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8167 | Visual Tracking / Lines Observation | 13,4,17,3,27,14,5,9,8 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8323 | Visual Tracking / Lines Observation | 17,3,6,4,6 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8324 | Visual Tracking / Lines Observation | 13,4,9,15,4,4 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8325 | Visual Tracking / Lines Observation | 14,5,9,4,7,10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 431 | Spatial Perception / 3D Views | A | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 514 | Spatial Perception / 3D Views | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 524 | Spatial Perception / 3D Views | A | `B` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 526 | Spatial Perception / 3D Views | 1-B,2-D,3-A,4-C | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | `1-A, 2-B, 3-C, 4-D` (❌) | **0.0%** |
| 527 | Spatial Perception / 3D Views | E | `N/A` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 548 | Spatial Perception / 3D Views | A | `C` (❌) | `A` (✅) | `C` (❌) | **33.3%** |
| 562 | Spatial Perception / 3D Views | A | `D` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 694 | Spatial Perception / 3D Views | D | `E` (❌) | `E` (❌) | `E` (❌) | **0.0%** |
| 696 | Spatial Perception / 3D Views | D | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 713 | Spatial Perception / 3D Views | C | `D` (❌) | `N/A` (❌) | `C` (✅) | **33.3%** |
| 886 | Spatial Perception / 3D Views | C | `B` (❌) | `C` (✅) | `B` (❌) | **33.3%** |
| 888 | Spatial Perception / 3D Views | C | `B` (❌) | `A` (❌) | `A` (❌) | **0.0%** |
| 2004 | Spatial Perception / 3D Views | A | `C` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 4047 | Spatial Perception / 3D Views | A-3,B-1,C-4,D-2,F-5,G-6,E-7,H-8 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5285 | Spatial Perception / 3D Views | 1-15,2-12,3-14,4-11,5-9,6-16,7-13,8-10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5340 | Spatial Perception / 3D Views | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 5432 | Spatial Perception / 3D Views | C | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 5694 | Spatial Perception / 3D Views | B | `C` (❌) | `B` (✅) | `B` (✅) | **66.7%** |
| 5695 | Spatial Perception / 3D Views | A | `N/A` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 6038 | Spatial Perception / 3D Views | 1-4,2-10,6-8,7-9,11-5,12-3 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6197 | Spatial Perception / 3D Views | 2-8, 1-3, 5-6, 4-7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6220 | Spatial Perception / 3D Views | 1-12,3-2,5-8,7-4,9-6,11-10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6280 | Spatial Perception / 3D Views | 1-C, 2-D, 3-A, 4-B. | `N/A` (❌) | `N/A` (❌) | `1-A` (❌) | **0.0%** |
| 6340 | Spatial Perception / 3D Views | 1-8,2-9,3-6,10-4,11-7,12-5 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6378 | Spatial Perception / 3D Views | C | `C` (✅) | `F` (❌) | `N/A` (❌) | **33.3%** |
| 6381 | Spatial Perception / 3D Views | 1-2, 4-7,5-10,8-3,9-6 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6434 | Spatial Perception / 3D Views | 1-4,3-2,6-5,8-7 | `1-5,3-2,6-4,8-7` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 799 | Spatial Perception / 3D Cube Unfold | 6,7,9 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1974 | Spatial Perception / 3D Cube Unfold | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 2065 | Spatial Perception / 3D Cube Unfold | The first one in the first row, the third one i... | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 3838 | Spatial Perception / 3D Cube Unfold | 3, 5, 6 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4064 | Spatial Perception / 3D Cube Unfold | E | `D` (❌) | `A` (❌) | `B` (❌) | **0.0%** |
| 4077 | Spatial Perception / 3D Cube Unfold | CD | `D` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4759 | Spatial Perception / 3D Cube Unfold | B,C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 4760 | Spatial Perception / 3D Cube Unfold | 2,5 | `6` (❌) | `2` (❌) | `2` (❌) | **0.0%** |
| 5388 | Spatial Perception / 3D Cube Unfold | 2,3,6 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5449 | Spatial Perception / 3D Cube Unfold | 2,5,7 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 6344 | Spatial Perception / 3D Cube Unfold | C | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 6467 | Spatial Perception / 3D Cube Unfold | A | `N/A` (❌) | `C` (❌) | `D` (❌) | **0.0%** |
| 501 | Spatial Perception / Paper Folding | D | `F` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 893 | Spatial Perception / Paper Folding | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 1217 | Spatial Perception / Paper Folding | B | `B` (✅) | `B` (✅) | `C` (❌) | **66.7%** |
| 3234 | Spatial Perception / Paper Folding | D | `C` (❌) | `C` (❌) | `F` (❌) | **0.0%** |
| 3240 | Spatial Perception / Paper Folding | F | `D` (❌) | `D` (❌) | `C` (❌) | **0.0%** |
| 4009 | Spatial Perception / Paper Folding | 1, 2, 3, 1 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 8333 | Spatial Perception / Paper Folding | 7 | `4` (❌) | `4` (❌) | `4` (❌) | **0.0%** |
| 8334 | Spatial Perception / Paper Folding | 7 | `3` (❌) | `3` (❌) | `3` (❌) | **0.0%** |
| 8335 | Spatial Perception / Paper Folding | 6 | `3` (❌) | `6` (✅) | `6` (✅) | **66.7%** |
| 8336 | Spatial Perception / Paper Folding | 8 | `3` (❌) | `5` (❌) | `6` (❌) | **0.0%** |
| 8337 | Spatial Perception / Paper Folding | 4 | `4` (✅) | `4` (✅) | `4` (✅) | **100.0%** |
| 8338 | Spatial Perception / Paper Folding | 9 | `5` (❌) | `N/A` (❌) | `5` (❌) | **0.0%** |
| 454 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `B` (❌) | `C` (❌) | **0.0%** |
| 480 | Spatial Perception / 3D Pattern Completion | C | `C` (✅) | `B` (❌) | `A` (❌) | **33.3%** |
| 481 | Spatial Perception / 3D Pattern Completion | A | `A` (✅) | `A` (✅) | `B` (❌) | **66.7%** |
| 484 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `A` (✅) | `C` (❌) | **33.3%** |
| 502 | Spatial Perception / 3D Pattern Completion | B | `A` (❌) | `N/A` (❌) | `B` (✅) | **33.3%** |
| 505 | Spatial Perception / 3D Pattern Completion | C | `A` (❌) | `A` (❌) | `B` (❌) | **0.0%** |
| 512 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 621 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `A` (✅) | `Choices: (A)` (✅) | **66.7%** |
| 3777 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 4375 | Spatial Perception / 3D Pattern Completion | B | `B` (✅) | `B` (✅) | `B` (✅) | **100.0%** |
| 4391 | Spatial Perception / 3D Pattern Completion | C | `B` (❌) | `C` (✅) | `C` (✅) | **66.7%** |
| 4420 | Spatial Perception / 3D Pattern Completion | A | `N/A` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 4735 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `A` (✅) | `A` (✅) | **66.7%** |
| 5308 | Spatial Perception / 3D Pattern Completion | C | `B` (❌) | `N/A` (❌) | `B` (❌) | **0.0%** |
| 5320 | Spatial Perception / 3D Pattern Completion | A | `B` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 5525 | Spatial Perception / 3D Pattern Completion | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 5531 | Spatial Perception / 3D Pattern Completion | B | `B` (✅) | `A` (❌) | `A` (❌) | **33.3%** |
| 6430 | Spatial Perception / 3D Pattern Completion | C | `N/A` (❌) | `A` (❌) | `D` (❌) | **0.0%** |
| 4453 | Spatial Perception / Count 3D blocks | 7 | `7` (✅) | `6` (❌) | `6` (❌) | **33.3%** |
| 4456 | Spatial Perception / Count 3D blocks | 7 | `7` (✅) | `7` (✅) | `8` (❌) | **66.7%** |
| 4457 | Spatial Perception / Count 3D blocks | 8 | `4` (❌) | `6` (❌) | `5` (❌) | **0.0%** |
| 4458 | Spatial Perception / Count 3D blocks | 10 | `11` (❌) | `9` (❌) | `10` (✅) | **33.3%** |
| 4460 | Spatial Perception / Count 3D blocks | 9 | `10` (❌) | `9` (✅) | `9` (✅) | **66.7%** |
| 4593 | Spatial Perception / Count 3D blocks | 9 | `6` (❌) | `7` (❌) | `6` (❌) | **0.0%** |
| 4594 | Spatial Perception / Count 3D blocks | 13 | `13` (✅) | `N/A` (❌) | `14` (❌) | **33.3%** |
| 4596 | Spatial Perception / Count 3D blocks | 13 | `10` (❌) | `11` (❌) | `9` (❌) | **0.0%** |
| 4597 | Spatial Perception / Count 3D blocks | 13 | `8` (❌) | `10` (❌) | `9` (❌) | **0.0%** |
| 4598 | Spatial Perception / Count 3D blocks | 16 | `10` (❌) | `7` (❌) | `11` (❌) | **0.0%** |
| 4599 | Spatial Perception / Count 3D blocks | 17 | `11` (❌) | `13` (❌) | `15` (❌) | **0.0%** |
| 4603 | Spatial Perception / Count 3D blocks | 17 | `9` (❌) | `10` (❌) | `N/A` (❌) | **0.0%** |
| 4604 | Spatial Perception / Count 3D blocks | 21 | `13` (❌) | `10` (❌) | `13` (❌) | **0.0%** |
| 4607 | Spatial Perception / Count 3D blocks | 26 | `12` (❌) | `13` (❌) | `14` (❌) | **0.0%** |
| 4610 | Spatial Perception / Count 3D blocks | 13 | `11` (❌) | `10` (❌) | `11` (❌) | **0.0%** |
| 4613 | Spatial Perception / Count 3D blocks | 15 | `12` (❌) | `11` (❌) | `12` (❌) | **0.0%** |
| 4614 | Spatial Perception / Count 3D blocks | 18 | `11` (❌) | `16` (❌) | `10` (❌) | **0.0%** |
| 4616 | Spatial Perception / Count 3D blocks | 23 | `27` (❌) | `27` (❌) | `27` (❌) | **0.0%** |
| 4618 | Spatial Perception / Count 3D blocks | 21 | `14` (❌) | `16` (❌) | `27` (❌) | **0.0%** |
| 4619 | Spatial Perception / Count 3D blocks | 21 | `17` (❌) | `27` (❌) | `15` (❌) | **0.0%** |
| 4621 | Spatial Perception / Count 3D blocks | 22 | `27` (❌) | `21` (❌) | `18` (❌) | **0.0%** |
| 4624 | Spatial Perception / Count 3D blocks | 19 | `13` (❌) | `N/A` (❌) | `10` (❌) | **0.0%** |
| 434 | Visual Pattern Recognition / Overlay Patterns | A | `B` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 435 | Visual Pattern Recognition / Overlay Patterns | 2,9 | `N/A` (❌) | `1,3` (❌) | `None` (❌) | **0.0%** |
| 438 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 441 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `N/A` (❌) | **0.0%** |
| 458 | Visual Pattern Recognition / Overlay Patterns | A | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 465 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 479 | Visual Pattern Recognition / Overlay Patterns | A | `N/A` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 504 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 509 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 536 | Visual Pattern Recognition / Overlay Patterns | 3,9 | `N/A` (❌) | `N/A` (❌) | `3,6` (❌) | **0.0%** |
| 625 | Visual Pattern Recognition / Overlay Patterns | C | `C` (✅) | `N/A` (❌) | `N/A` (❌) | **33.3%** |
| 664 | Visual Pattern Recognition / Overlay Patterns | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 693 | Visual Pattern Recognition / Overlay Patterns | C | `C` (✅) | `C` (✅) | `N/A` (❌) | **66.7%** |
| 708 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 3992 | Visual Pattern Recognition / Overlay Patterns | B | `A` (❌) | `C` (❌) | `A` (❌) | **0.0%** |
| 3993 | Visual Pattern Recognition / Overlay Patterns | A | `C` (❌) | `N/A` (❌) | `C` (❌) | **0.0%** |
| 4097 | Visual Pattern Recognition / Overlay Patterns | A | `B` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 362 | Visual Pattern Recognition / Logic Patterns | A | `C` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 448 | Visual Pattern Recognition / Logic Patterns | B | `D` (❌) | `N/A` (❌) | `D` (❌) | **0.0%** |
| 467 | Visual Pattern Recognition / Logic Patterns | F | `N/A` (❌) | `E` (❌) | `N/A` (❌) | **0.0%** |
| 487 | Visual Pattern Recognition / Logic Patterns | A | `N/A` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 553 | Visual Pattern Recognition / Logic Patterns | 1 | `7` (❌) | `1` (✅) | `8` (❌) | **33.3%** |
| 642 | Visual Pattern Recognition / Logic Patterns | C | `N/A` (❌) | `B` (❌) | `N/A` (❌) | **0.0%** |
| 657 | Visual Pattern Recognition / Logic Patterns | F | `E` (❌) | `(F)` (✅) | `N/A` (❌) | **33.3%** |
| 669 | Visual Pattern Recognition / Logic Patterns | A | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 676 | Visual Pattern Recognition / Logic Patterns | B | `C` (❌) | `N/A` (❌) | `D` (❌) | **0.0%** |
| 687 | Visual Pattern Recognition / Logic Patterns | E | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 718 | Visual Pattern Recognition / Logic Patterns | E | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1293 | Visual Pattern Recognition / Logic Patterns | D | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1914 | Visual Pattern Recognition / Logic Patterns | 2-9 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 1925 | Visual Pattern Recognition / Logic Patterns | 3 and 11 | `N/A` (❌) | `1\ \text{and}\ 12` (❌) | `N/A` (❌) | **0.0%** |
| 510 | Visual Pattern Recognition / Rotation Patterns | 6,4,2 | `1, 2, 3` (❌) | `1, 2, 3` (❌) | `1, 2, 3` (❌) | **0.0%** |
| 540 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `B` (✅) | `A` (❌) | **33.3%** |
| 631 | Visual Pattern Recognition / Rotation Patterns | F | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 684 | Visual Pattern Recognition / Rotation Patterns | C | `N/A` (❌) | `B` (❌) | `A` (❌) | **0.0%** |
| 4180 | Visual Pattern Recognition / Rotation Patterns | C | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |
| 5293 | Visual Pattern Recognition / Rotation Patterns | B | `N/A` (❌) | `D` (❌) | `C` (❌) | **0.0%** |
| 5519 | Visual Pattern Recognition / Rotation Patterns | C | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 5565 | Visual Pattern Recognition / Rotation Patterns | B | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 6455 | Visual Pattern Recognition / Rotation Patterns | B | `C` (❌) | `C` (❌) | `C` (❌) | **0.0%** |
| 6462 | Visual Pattern Recognition / Rotation Patterns | B | `B` (✅) | `N/A` (❌) | `C` (❌) | **33.3%** |
| 537 | Visual Pattern Recognition / Mirroring Patterns | D | `C` (❌) | `B` (❌) | `B` (❌) | **0.0%** |
| 538 | Visual Pattern Recognition / Mirroring Patterns | 1-2,3-6,4-5 | `1-4, 2-5, 3-6` (❌) | `N/A` (❌) | `No pairs can be identified as mirror images bas...` (❌) | **0.0%** |
| 547 | Visual Pattern Recognition / Mirroring Patterns | 8 | `9` (❌) | `9` (❌) | `9` (❌) | **0.0%** |
| 773 | Visual Pattern Recognition / Mirroring Patterns | 1-4,2-5,3-6 | `1-2, 3-4, 5-6` (❌) | `1-2, 3-4, 5-6` (❌) | `1-6, 2-5, 3-4` (❌) | **0.0%** |
| 819 | Visual Pattern Recognition / Mirroring Patterns | C | `D` (❌) | `D` (❌) | `D` (❌) | **0.0%** |
| 1929 | Visual Pattern Recognition / Mirroring Patterns | 1-7, 2-4, 3-10, 5-11, 6-8, 9-12 | `1-4, 2-3, 5-8, 6-7, 9-10, 11-12` (❌) | `1-4, 2-3` (❌) | `1-10, 8-11` (❌) | **0.0%** |
| 3691 | Visual Pattern Recognition / Mirroring Patterns | C | `C` (✅) | `C` (✅) | `C` (✅) | **100.0%** |
| 4769 | Visual Pattern Recognition / Mirroring Patterns | 1-6, 2-7, 3-4, 5-10, 8-12, 9-11 | `1-3,2-4,5-7,6-9,8-10,11-12` (❌) | `1-3,2-4,5-7,6-10,8-11,9-12` (❌) | `N/A` (❌) | **0.0%** |
| 4785 | Visual Pattern Recognition / Mirroring Patterns | 1-7, 2-4, 3-5, 6-8 | `8-7` (❌) | `1-8, 2-7, 3-6, 4-5` (❌) | `1-8` (❌) | **0.0%** |
| 5288 | Visual Pattern Recognition / Mirroring Patterns | 1-6,2-11,3-9,4-12,5-7,8-10 | `N/A` (❌) | `N/A` (❌) | `N/A` (❌) | **0.0%** |