"""
Polished Storyboard PDF Generator
Generates storyboard/storyboard.pdf using ReportLab with professional academic styling.
"""

import sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.append(str(PROJECT_ROOT))
from config import STUDENT_NAME, STUDENT_ID, COURSE_NAME, VIDEO_TITLE, TOPIC

def generate_pdf():
    pdf_path = PROJECT_ROOT / "storyboard" / "storyboard.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    primary_color = colors.HexColor("#1A1A2E")
    accent_color = colors.HexColor("#0F3460")
    highlight_color = colors.HexColor("#E94560")
    dark_gray = colors.HexColor("#2B2D42")
    light_bg = colors.HexColor("#F8F9FA")
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        alignment=1, # Center
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=16,
        textColor=accent_color,
        alignment=1,
        spaceAfter=15
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=dark_gray,
        alignment=1,
        spaceAfter=20
    )
    
    scene_header_style = ParagraphStyle(
        'SceneHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.white,
        spaceAfter=0
    )
    
    field_label_style = ParagraphStyle(
        'FieldLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=accent_color
    )
    
    field_content_style = ParagraphStyle(
        'FieldContent',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=dark_gray
    )
    
    story = []
    
    # Header block
    story.append(Paragraph("M3 MATHEMATICS ANIMATION VIDEO PROJECT", subtitle_style))
    story.append(Paragraph(VIDEO_TITLE, title_style))
    story.append(Paragraph(
        f"<b>Student Name:</b> {STUDENT_NAME} &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"<b>Student ID:</b> {STUDENT_ID} &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"<b>Topic:</b> {TOPIC}<br/>"
        f"<b>Format:</b> 1080p 60 FPS &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"<b>Aspect Ratio:</b> 16:9 &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"<b>Target Duration:</b> ~5 mins 10 secs",
        meta_style
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent_color, spaceAfter=18))
    
    # Six scenes data
    scenes = [
        {
            "num": "SCENE 1",
            "title": "Hook / Context",
            "duration": "00:00 – 00:35 (35 seconds)",
            "objective": "Engage viewers with real-world applications of linear transformations (game engines, computer graphics, physics) and pose the core question: How does a matrix transform space?",
            "equations": "T(v) = Av  |  A = [[a, b], [c, d]]",
            "visuals": "Slate dark background (#14141E) with subtle grid lines. Test vector navigates plane. Matrix transforms space smoothly. Opening title card displays student name, student ID, and video title.",
            "narration": "Have you ever wondered how computer graphics rotate a character or game engines warp space? A matrix is not just a spreadsheet—it is a geometric engine that stretches, rotates, and reshapes space...",
            "animation": "1. Fade in plane. 2. Vector movement across grid. 3. Dramatic grid warp via matrix [[2,1],[1,2]]. 4. Display title and student metadata. 5. Crossfade.",
            "transition": "Smooth cross-fade to Scene 2."
        },
        {
            "num": "SCENE 2",
            "title": "Concept Introduction & Linearity Axioms",
            "duration": "00:35 – 01:25 (50 seconds)",
            "objective": "Formally define linear transformation: T(v) = Av. Establish additivity T(u+v)=T(u)+T(v), homogeneity T(cu)=cT(u), and origin preservation T(0)=0.",
            "equations": "T(u + v) = T(u) + T(v)   |   T(c·u) = c·T(u)   |   T(0) = 0   |   Non-linear: T(v) = v + b",
            "visuals": "Left panel displays formal definitions. Right panel displays vector addition parallelogram and scalar scaling. Highlight origin with warning showing affine shifts violate linearity.",
            "narration": "In mathematics, a transformation is a function mapping vectors to vectors: T(v) = Av. It must satisfy additivity and homogeneity. Crucially, the origin must remain fixed: T(0) = 0...",
            "animation": "1. Function notation reveal. 2. Vector addition tip-to-tail animation. 3. Vector scaling. 4. Origin callout and affine non-example demonstration.",
            "transition": "Slide transition into Scene 3."
        },
        {
            "num": "SCENE 3",
            "title": "Visual Intuition & Basis Tracking",
            "duration": "01:25 – 02:25 (60 seconds)",
            "objective": "Demonstrate that tracking standard basis vectors e1 and e2 completely determines the transformation of the entire 2D plane.",
            "equations": "e₁ = (1, 0)ᵀ ⟹ T(e₁) = (2, 1)ᵀ   |   e₂ = (0, 1)ᵀ ⟹ T(e₂) = (1, 2)ᵀ   |   A = [[2, 1], [1, 2]]",
            "visuals": "Standard grid with red e1 and green e2. Unit square shaded in cyan. Grid smoothly deforms as e1->(2,1) and e2->(1,2). Unit square becomes purple parallelogram with vertices (0,0),(2,1),(3,3),(1,2).",
            "narration": "How do we visualize what a matrix does? Look at basis vectors e1 and e2. In matrix A, column 1 is (2,1) and column 2 is (1,2). The matrix columns are literally the landing sites of basis vectors!",
            "animation": "1. Plot e1, e2, and unit square. 2. Highlight matrix columns. 3. Smooth continuous plane transformation. 4. Track parallelogram vertices (0,0), (2,1), (3,3), (1,2).",
            "transition": "Wipe right to Scene 4."
        },
        {
            "num": "SCENE 4",
            "title": "Worked Example: Step-by-Step Multiplication",
            "duration": "02:25 – 03:25 (60 seconds)",
            "objective": "Step-by-step arithmetic computation of matrix multiplication for two distinct test vectors, linking algebraic calculations to animated vectors on the grid.",
            "equations": "A(1, 1) = [2(1)+1(1); 1(1)+2(1)] = (3, 3)ᵀ   |   A(2, -1) = [2(2)+1(-1); 1(2)+2(-1)] = (3, 0)ᵀ",
            "visuals": "Split screen: Step-by-step arithmetic reveals on left; coordinate plane on right. Blue vector (1,1) moves along diagonal to (3,3). Gold vector (2,-1) rotates and lands directly on positive x-axis at (3,0).",
            "narration": "Let us verify algebraically. For v1 = (1,1): 2(1)+1(1)=3, 1(1)+2(1)=3, giving (3,3). For v2 = (2,-1): 2(2)-1=3, 1(2)-2=0, giving (3,0). Algebra and geometry agree in perfect harmony.",
            "animation": "1. Show v1 on grid. 2. Reveal row-by-column arithmetic. 3. Animate v1 stretching to (3,3). 4. Show v2. 5. Reveal arithmetic. 6. Animate v2 landing on (3,0).",
            "transition": "Morph transition to Scene 5."
        },
        {
            "num": "SCENE 5",
            "title": "Geometric Interpretation: Determinant & Eigenvalues",
            "duration": "03:25 – 04:35 (70 seconds)",
            "objective": "Explain determinant as area scaling, analyze eigenvector invariant directions, and contrast area preservation with rigid rotation (isometry).",
            "equations": "det(A) = 2·2 - 1·1 = 3   |   λ₁ = 3, v=(1,1)   |   λ₂ = 1, v=(1,-1)   |   B = [[2, 0], [0, 0.5]], det(B) = 1",
            "visuals": "Parallelogram area measurement showing 3x expansion. Pink invariant line along (1,1) stretching by 3; blue line along (1,-1) preserving length. Unit square squashing into 2x0.5 rectangle under matrix B.",
            "narration": "The determinant gives the area scaling factor: area 1 expands to 3. det > 0 preserves orientation. Eigenvectors reveal invariant scaling axes. Finally, det(B)=1 preserves area, but is NOT a rigid rotation!",
            "animation": "1. Compute det(A)=3 and show area tripling. 2. Highlight eigenvector scaling along (1,1) and (1,-1). 3. Animate squeeze matrix B. 4. Display callout distinguishing area vs length preservation.",
            "transition": "Dissolve into Scene 6."
        },
        {
            "num": "SCENE 6",
            "title": "Summary & Academic Credits",
            "duration": "04:35 – 05:10 (35 seconds)",
            "objective": "Synthesize the 5 key takeaways of the presentation and display complete project and student submission credits.",
            "equations": "Summary of: Linearity, Basis Columns, Grid Morph, Determinant Area Factor, Eigenspace",
            "visuals": "Bulleted summary card with 5 core insights. Final academic submission card displaying project title, student name, student ID, software dependencies, and closing fade to black.",
            "narration": "To summarize: linear transformations preserve parallel lines and origin; matrix columns encode basis landing sites; determinant measures area scaling; and area preservation does not imply distance preservation.",
            "animation": "1. Sequentially reveal the 5 takeaways. 2. Transition to closing credits frame with student details. 3. Fade out to black.",
            "transition": "Fade out to black (End of Video)."
        }
    ]
    
    for idx, sc in enumerate(scenes):
        header_text = f"<b>{sc['num']}: {sc['title']}</b>"
        header_p = Paragraph(header_text, scene_header_style)
        
        # Header banner table
        header_table = Table([[header_p]], colWidths=[522])
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), accent_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        
        content_data = [
            [Paragraph("<b>Duration</b>", field_label_style), Paragraph(sc["duration"], field_content_style)],
            [Paragraph("<b>Learning Objective</b>", field_label_style), Paragraph(sc["objective"], field_content_style)],
            [Paragraph("<b>Key Equations</b>", field_label_style), Paragraph(f"<code>{sc['equations']}</code>", field_content_style)],
            [Paragraph("<b>Visual Direction</b>", field_label_style), Paragraph(sc["visuals"], field_content_style)],
            [Paragraph("<b>Narration Summary</b>", field_label_style), Paragraph(sc["narration"], field_content_style)],
            [Paragraph("<b>Animation Flow</b>", field_label_style), Paragraph(sc["animation"], field_content_style)],
            [Paragraph("<b>Scene Transition</b>", field_label_style), Paragraph(sc["transition"], field_content_style)],
        ]
        
        content_table = Table(content_data, colWidths=[110, 412])
        content_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), light_bg),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#DCDDE1")),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        
        block = KeepTogether([header_table, content_table, Spacer(1, 14)])
        story.append(block)
        
    doc.build(story)
    print(f"✓ Storyboard PDF compiled successfully: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
